import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['month_begin_date', 'geo', 'age_group', 'sex']
)

@pytest.fixture
def unemployment_monthly_snapshot():
    df = pd.read_sql("select * from stg.unemployment_monthly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/unemployment_monthly_snapshot.html")
    return df

@pytest.fixture
def unemployment_monthly_snapshot_filtered(unemployment_monthly_snapshot):
    return unemployment_monthly_snapshot.query(
        "sex == 'Both sexes' and age_group == '15 years and over'"
    )

def test_processed_unique_column_set(unemployment_monthly_snapshot, unemployment_monthly_snapshot_filtered):
    prepped_test_suite.test_for_unique_column_set(unemployment_monthly_snapshot)
    prepped_test_suite.test_for_unique_column_set(unemployment_monthly_snapshot_filtered)
    
def test_processed_non_null_cols(unemployment_monthly_snapshot_filtered):
    prepped_test_suite.test_for_nulls(
        # unemployment_monthly_snapshot, # these do have nulls
        unemployment_monthly_snapshot_filtered,
        non_null_cols=['month_begin_date', 'geo', 'age_group', 'sex', 'unemployment_rate']
    )

def test_processed_for_holes(unemployment_monthly_snapshot_filtered):
    # prepped_test_suite.test_for_holes(unemployment_monthly_snapshot) # these do have holes
    prepped_test_suite.test_for_holes(unemployment_monthly_snapshot_filtered)