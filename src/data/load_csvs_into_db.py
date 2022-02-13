import pandas as pd
from sqlalchemy import create_engine
from pandas_profiling import ProfileReport
from settings import ENGINE_PATH
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

def load():
    # loading csvs
    earnings_df = pd.read_csv("./data/raw/earnings-14100223-eng/14100223.csv").infer_objects()
    emissions_df = pd.read_csv("./data/raw/emissions-38100097-eng/38100097.csv").infer_objects()
    gdp_df = pd.read_csv("./data/raw/gdp-36100402-eng/36100402.csv").infer_objects()
    gdp_monthly_df = pd.read_csv("./data/raw/gdp-can-monthly-36100434-eng/36100434.csv").infer_objects()
    labour_force_df = pd.read_csv("./data/raw/labour-force-14100287-eng/14100287.csv").infer_objects()
    low_income_df = pd.read_csv("./data/raw/low-income-11100135-eng/11100135.csv").infer_objects()
    prices_df = pd.read_csv("./data/raw/prices-18100004-eng/18100004.csv").infer_objects()

    # profiling the raw data
    profile = ProfileReport(earnings_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/monthly_earnings.html")
    profile = ProfileReport(emissions_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/yearly_emissions.html")
    profile = ProfileReport(gdp_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/yearly_gdp.html")
    profile = ProfileReport(gdp_monthly_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/monthly_gdp.html")
    profile = ProfileReport(labour_force_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/monthly_labour_force.html")
    profile = ProfileReport(low_income_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/yearly_low_income.html")
    profile = ProfileReport(prices_df, title="Raw Pandas Profiling Report", minimal=True)
    profile.to_file("./reports/eda_reports/raw/monthly_prices.html")

    # saving raw data to db
    earnings_df.to_sql(con=conn, name="monthly_earnings", schema="src", if_exists="replace", index=True)
    emissions_df.to_sql(con=conn, name="yearly_emissions", schema="src", if_exists="replace", index=True)
    gdp_df.to_sql(con=conn, name="yearly_gdp", schema="src", if_exists="replace", index=True)
    gdp_monthly_df.to_sql(con=conn, name="monthly_gdp", schema="src", if_exists="replace", index=True)
    labour_force_df.to_sql(con=conn, name="monthly_labour_force", schema="src", if_exists="replace", index=True)
    low_income_df.to_sql(con=conn, name="yearly_low_income", schema="src", if_exists="replace", index=True)
    prices_df.to_sql(con=conn, name="monthly_prices", schema="src", if_exists="replace", index=True)

if __name__ == "__main__":
    load()