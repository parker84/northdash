import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['year_begin_date', 'industry', 'geo']
)

@pytest.fixture
def provincial_gdp_yearly_snapshot():
    df = pd.read_sql("select * from stg.provincial_gdp_yearly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/provincial_gdp_yearly_snapshot.html")
    return df

@pytest.fixture
def provincial_gdp_yearly_snapshot_filtered(provincial_gdp_yearly_snapshot):
    return provincial_gdp_yearly_snapshot.query(
        "industry == 'All industries [T001]'"
    )

def test_processed_unique_column_set(provincial_gdp_yearly_snapshot):
    prepped_test_suite.test_for_unique_column_set(provincial_gdp_yearly_snapshot)
    
def test_processed_non_null_cols(provincial_gdp_yearly_snapshot, provincial_gdp_yearly_snapshot_filtered):
    prepped_test_suite.test_for_nulls(
        provincial_gdp_yearly_snapshot,
        non_null_cols=['year_begin_date', 'industry']
    )

def test_processed_for_holes(provincial_gdp_yearly_snapshot):
    prepped_test_suite.test_for_holes(provincial_gdp_yearly_snapshot)