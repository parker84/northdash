import streamlit as st
import datetime
import plotly.express as px
import pandas as pd
from settings import ENGINE_PATH
from sqlalchemy import create_engine
import sqlalchemy
engine = create_engine(ENGINE_PATH)
conn = engine.connect()

#-------constants
GEO_OPTIONS = [
    'Canada',
    'Alberta', 
    'British Columbia', 
    'Manitoba', 
    'New Brunswick', 
    'Newfoundland and Labrador', 
    'Northwest Territories', 
    'Nova Scotia', 
    'Nunavut', 
    'Ontario', 
    'Prince Edward Island', 
    'Quebec', 
    'Saskatchewan', 
    'Yukon'
]

#--------loaders
@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_monthly_earnings_all_industries(start_date, end_date, geo):
    with open('./src/visualization/sql_queries/get_monthly_earnings_all_industries.sql', 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_yearly_emissions_all_sectors(start_date, end_date, geo):
    with open('./src/visualization/sql_queries/get_yearly_emissions_all_sectors.sql', 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_gdp_all_industries(start_date, end_date, geo):
    if geo == 'Canada':
        file_path = './src/visualization/sql_queries/get_canada_gdp_all_industries.sql'
    else:
        file_path = './src/visualization/sql_queries/get_provincial_gdp_all_industries.sql'
    with open(file_path, 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_monthly_population(start_date, end_date, geo):
    with open('./src/visualization/sql_queries/get_monthly_population.sql', 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_monthly_unemployment_rate(start_date, end_date, geo):
    with open('./src/visualization/sql_queries/get_monthly_unemployment_rate.sql', 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

@st.cache(hash_funcs={sqlalchemy.engine.base.Connection: id})
def get_yearly_low_income_rate(start_date, end_date, geo):
    with open('./src/visualization/sql_queries/get_yearly_low_income_rate.sql', 'r') as f:
        query = f.read().format(
            start_date=start_date,
            end_date=end_date,
            geo=geo
        )
    df = pd.read_sql(query, con=conn)
    return df

#------helpers
def viz_status_metric(df, x_axis, y_axis, metric_value, title, delta_color='normal'):
    if x_axis == 'month_begin_date':
        yoy_diff_int = 12
    elif x_axis == 'year_begin_date':
        yoy_diff_int = 1
    st.metric(
        title, 
        value=metric_value, 
        delta='{}% Year over Year'.format(
            round(100*((df[y_axis].iloc[0] 
            / df[y_axis].iloc[yoy_diff_int])-1), 2)
        ),
        delta_color=delta_color
    )
    fig = px.line(
        df, x=x_axis, y=y_axis, title=title, width=350, height=350)
    st.plotly_chart(fig, use_container_width=True)

#------dash setup
st.set_page_config(
    layout='wide', 
    page_icon='🍁',
    page_title='NorthDash',
    menu_items={
        'Get Help': 'https://join.slack.com/t/northdashworkspace/shared_invite/zt-13znumtxg-TTnPqSFOzXMV18lg~TsILQ',
        'Report a bug': "https://github.com/parker84/north-dash/issues/new",
        'About': "This dashboard was initially created by [Brydon Parker](https://linkpop.com/brydon)."
    }
)
st.title('Canada Status Dashboard')
st.markdown("This dashboard provides a high level overview of critical metrics for 🇨🇦 Canada and each of it's provinces.")

with st.expander('README', expanded=False):
    st.markdown(
    """
    ### Caveats:
    1. Not all data sources start and end at the same time.
    2. Metrics are colored based good/bad, so if emissions for example are increasing year over year they will be colored as red.
    3. Population is only estimated for those 15 years of age and older.

    ### Definitions:
    1. GDP: 
    2. GDP per Capita:
    3. Avg Weekly Earnings: 
    4. Avg Price: 
    5. Population: 
    6. % Low Income: 
    7. % Unemployed: 
    8. Yearly Emissions: 

    ### Tips:
    1. You can zoom in on any graph by clicking and dragging a box on the graph where you want to zoom.
    2. For each parameter (ex: Province/Country), if you hover over the "(?)" (top right of parameter) you can see more detailed instructions for that parameter. 
    3. Have questions/feedback? Join our [slack workspace](https://join.slack.com/t/northdashworkspace/shared_invite/zt-13znumtxg-TTnPqSFOzXMV18lg~TsILQ)

    ### Sections:
    1. **TL;DR**: Metric summaries
    2. **Economic Deep Dive**: Detailed economic metrics and breakdowns by industry and province
    3. **Social Deep Dive**: Detailed social metrics and breakdowns by province
    4. **Environmental Deep Dive**: Detailed environmental metrics and breakdowns by province
    5. **Data**: Links and descriptions of each data source used in this dashboard
    """
    )


#-------sidebar setup
st.sidebar.title('🍁NorthDash')
geo = st.sidebar.selectbox(
    'Choose Province/Country', 
    GEO_OPTIONS, 
    help='If you want to see metrics for a specific province instead of all of Canada, you can choose which province here.'
)
with st.sidebar.expander('More Parameter Options', expanded=False):
    start_date = str(st.date_input(
        'Start Date', 
        datetime.date(1900, 1, 1),
        help='Date to start all chart at. If this date is earlier than the first date in the data source, we will show the back to the earliest data from the data source.'
    ))
    end_date = str(st.date_input(
        'End Date', 
        datetime.datetime.now(),
        help='Date to end all charts at. If this date is after the last date in the data source, we will show up to the last data from the data source.'
    ))

st.sidebar.markdown(
    """
    Have questions/feedback? Join our [slack workspace](https://join.slack.com/t/northdashworkspace/shared_invite/zt-13znumtxg-TTnPqSFOzXMV18lg~TsILQ)
    
    Like 🍁Northdash and want to say thanks?       
    [:coffee: buy me a coffee](https://www.buymeacoffee.com/brydon)
    """
)

#-------key metrics
st.header('Section 1: TL;DR')
st.markdown('Metric summaries')

st.subheader('Economic Metrics')
col1, col2, col3, col4 = st.columns(4)
gdp_all_industries = get_gdp_all_industries(start_date, end_date, geo)
with col1: 
    if geo == 'Canada':
        viz_status_metric(
            gdp_all_industries, 
            x_axis='month_begin_date',
            y_axis='gdp',
            metric_value="${:,.3f}T".format(gdp_all_industries.gdp.iloc[0]/1e+12),
            title='GDP'
        )
    else:
        viz_status_metric(
            gdp_all_industries, 
            x_axis='year_begin_date',
            y_axis='gdp',
            metric_value="${:,.3f}T".format(gdp_all_industries.gdp.iloc[0]/1e+12),
            title='GDP'
        )
with col2: 
    if geo == 'Canada':
        viz_status_metric(
            gdp_all_industries, 
            x_axis='month_begin_date',
            y_axis='gdp_per_capita',
            metric_value="${:,.0f}".format(gdp_all_industries.gdp_per_capita.iloc[0]),
            title='GDP per Capita'
        )
    else:
        viz_status_metric(
            gdp_all_industries, 
            x_axis='year_begin_date',
            y_axis='gdp_per_capita',
            metric_value="${:,.0f}".format(gdp_all_industries.gdp_per_capita.iloc[0]),
            title='GDP per Capita'
        )
with col3: 
    monthly_earnings_all_industries = get_monthly_earnings_all_industries(start_date, end_date, geo)
    viz_status_metric(
            monthly_earnings_all_industries, 
            x_axis='month_begin_date',
            y_axis='avg_weekly_earnings',
            metric_value="${:,.2f}".format(monthly_earnings_all_industries.avg_weekly_earnings.iloc[0]),
            title='Avg Weekly Earnings'
    )
with col4: 
    st.metric('Avg Price', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=300, height=300)
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Social/Environmental Metrics')
col1, col2, col3, col4 = st.columns(4)
with col1: 
    monthly_population = get_monthly_population(start_date, end_date, geo)
    viz_status_metric(
        monthly_population, 
        x_axis='month_begin_date',
        y_axis='population',
        metric_value="{:,.1f}M".format(monthly_population.population.iloc[0] / 1e+06),
        title='Population'
    )
with col2: 
    yearly_low_income_rate = get_yearly_low_income_rate(start_date, end_date, geo)
    viz_status_metric(
        yearly_low_income_rate, 
        x_axis='year_begin_date',
        y_axis='low_income_rate',
        metric_value="{:,.1f}%".format(yearly_low_income_rate.low_income_rate.iloc[0]),
        title='Low Income Rate',
        delta_color='inverse'
    )
with col3: 
    monthly_unemployment_rate = get_monthly_unemployment_rate(start_date, end_date, geo)
    viz_status_metric(
        monthly_unemployment_rate, 
        x_axis='month_begin_date',
        y_axis='unemployment_rate',
        metric_value="{:,.1f}%".format(monthly_unemployment_rate.unemployment_rate.iloc[0]),
        title='Unemployment Rate',
        delta_color='inverse'
    )
with col4: 
    yearly_emissions_all_sectors = get_yearly_emissions_all_sectors(start_date, end_date, geo)
    viz_status_metric(
        yearly_emissions_all_sectors, 
        x_axis='year_begin_date',
        y_axis='yearly_kilotonnes',
        metric_value="{:,.2f}".format(yearly_emissions_all_sectors.yearly_kilotonnes.iloc[0]),
        title='Yearly Emissions',
        delta_color='inverse'
    )


#-------drill downs
with st.expander('Section 2: Economic Deep Dive', expanded=False):
    st.header('Section 2: Economic Deep Dive')
    st.markdown('Detailed economic metrics and breakdowns by industry and province')
    st.markdown('Coming Soon!')

with st.expander('Section 3: Social Deep Dive', expanded=False):
    st.header('Section 3: Social Deep Dive')
    st.markdown('Detailed social metrics and breakdowns by province')
    st.markdown('Coming Soon!')

with st.expander('Section 4: Environmental Deep Dive', expanded=False):
    st.header('Section 4: Environmental Deep Dive')
    st.markdown('Detailed environmental metrics and breakdowns by province')
    st.markdown('Coming Soon!')

with st.expander('Section 5: Data', expanded=False):
    st.header('Section 5: Data')
    st.markdown('Links and descriptions of each data source used in this dashboard')
    st.markdown(
    """
    ### StatsCan:
    1. [Physical flow account for greenhouse gas emissions, annual](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810009701)
    2. [Low income statistics by age, sex and economic family type, annual](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1110013501)
    3. [Gross domestic product (GDP) at basic prices, by industry, provinces and territories, annual (x 1,000,000)](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610040201)
    4. [Consumer Price Index, monthly, not seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401)
    5. [Labour force characteristics by province, monthly, seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410028703)
    6. [Gross domestic product (GDP) at basic prices, by industry, monthly (x 1,000,000)](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610043401)
    7. [Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301&pickMembers%5B0%5D=2.2&pickMembers%5B1%5D=3.1&cubeTimeFrame.startMonth=07&cubeTimeFrame.startYear=2021&cubeTimeFrame.endMonth=11&cubeTimeFrame.endYear=2021&referencePeriods=20210701%2C20211101)
    """
    )