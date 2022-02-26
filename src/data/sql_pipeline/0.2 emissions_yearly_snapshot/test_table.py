import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['year_begin_date', 'sector', 'geo']
)

@pytest.fixture
def emissions_yearly_snapshot():
    df = pd.read_sql("select * from stg.emissions_yearly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/emissions_yearly_snapshot.html")
    return df

@pytest.fixture
def emissions_yearly_snapshot_filtered(emissions_yearly_snapshot):
    return emissions_yearly_snapshot.query(
        "sector == 'Total, industries and households'"
    )

def test_processed_unique_column_set(emissions_yearly_snapshot):
    prepped_test_suite.test_for_unique_column_set(emissions_yearly_snapshot)
    
def test_processed_non_null_cols(emissions_yearly_snapshot, emissions_yearly_snapshot_filtered):
    prepped_test_suite.test_for_nulls(
        emissions_yearly_snapshot,
        non_null_cols=['year_begin_date', 'sector']
    )
    prepped_test_suite.test_for_nulls(
        emissions_yearly_snapshot_filtered,
        non_null_cols=['year_begin_date', 'sector', 'yearly_kilotonnes']
    )

def test_processed_for_holes(emissions_yearly_snapshot_filtered):
    prepped_test_suite.test_for_holes(emissions_yearly_snapshot_filtered)