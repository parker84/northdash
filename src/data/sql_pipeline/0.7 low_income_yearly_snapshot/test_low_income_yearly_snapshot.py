import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['year_begin_date', 'geo', 'demographic']
)

@pytest.fixture
def low_income_yearly_snapshot():
    df = pd.read_sql("select * from stg.low_income_yearly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/low_income_yearly_snapshot.html")
    return df

@pytest.fixture
def low_income_yearly_snapshot_filtered(low_income_yearly_snapshot):
    return low_income_yearly_snapshot.query(
        "demographic == 'All persons'"
    )

def test_processed_unique_column_set(low_income_yearly_snapshot, low_income_yearly_snapshot_filtered):
    prepped_test_suite.test_for_unique_column_set(low_income_yearly_snapshot)
    prepped_test_suite.test_for_unique_column_set(low_income_yearly_snapshot_filtered)
    
def test_processed_non_null_cols(low_income_yearly_snapshot_filtered):
    prepped_test_suite.test_for_nulls(
        # low_income_yearly_snapshot, # these do have nulls
        low_income_yearly_snapshot_filtered,
        non_null_cols=['year_begin_date', 'geo', 'demographic', 'low_income_rate']
    )

def test_processed_for_holes(low_income_yearly_snapshot):
    prepped_test_suite.test_for_holes(low_income_yearly_snapshot)