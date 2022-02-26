import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['month_begin_date', 'industry']
)

@pytest.fixture
def canada_gdp_monthly_snapshot():
    df = pd.read_sql("select * from stg.canada_gdp_monthly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/canada_gdp_monthly_snapshot.html")
    return df

def test_processed_unique_column_set(canada_gdp_monthly_snapshot):
    prepped_test_suite.test_for_unique_column_set(canada_gdp_monthly_snapshot)
    
def test_processed_non_null_cols(canada_gdp_monthly_snapshot):
    prepped_test_suite.test_for_nulls(
        canada_gdp_monthly_snapshot,
        non_null_cols=['month_begin_date', 'industry']
    )
    prepped_test_suite.test_for_nulls(
        canada_gdp_monthly_snapshot[
            canada_gdp_monthly_snapshot.industry == 'All industries [T001]'
        ],
        non_null_cols=['month_begin_date', 'industry', 'gdp']
    )

def test_processed_for_holes(canada_gdp_monthly_snapshot):
    prepped_test_suite.test_for_holes(canada_gdp_monthly_snapshot)