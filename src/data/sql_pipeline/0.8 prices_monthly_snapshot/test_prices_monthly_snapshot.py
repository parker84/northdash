import pytest
from settings import ENGINE_PATH
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
import pandas as pd
import datetime
from src.utils.testing_suite import TestSuite
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

prepped_test_suite = TestSuite(
    unique_cols=['month_begin_date', 'geo', 'product_group']
)

@pytest.fixture
def prices_monthly_snapshot():
    df = pd.read_sql("select * from stg.prices_monthly_snapshot", con=conn)
    profile = ProfileReport(df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/processed/prices_monthly_snapshot.html")
    return df

@pytest.fixture
def prices_monthly_snapshot_filtered(prices_monthly_snapshot):
    out_df = prices_monthly_snapshot.query(
        "product_group == 'All-items'"
    )
    out_df = out_df[out_df.month_begin_date >= datetime.date(2005, 1, 1)]
    return out_df 

def test_processed_unique_column_set(prices_monthly_snapshot, prices_monthly_snapshot_filtered):
    prepped_test_suite.test_for_unique_column_set(prices_monthly_snapshot)
    prepped_test_suite.test_for_unique_column_set(prices_monthly_snapshot_filtered)
    
def test_processed_non_null_cols(prices_monthly_snapshot):
    prepped_test_suite.test_for_nulls(
        prices_monthly_snapshot, # these do have nulls
        non_null_cols=['month_begin_date', 'geo', 'product_group', 'consumer_price_index']
    )

def test_processed_for_holes(prices_monthly_snapshot_filtered):
    # prepped_test_suite.test_for_holes(prices_monthly_snapshot) # these do have holes, in part bc nunavut didn't become an official territory until 1999 
    prepped_test_suite.test_for_holes(prices_monthly_snapshot_filtered)