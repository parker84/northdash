import streamlit as st
import datetime
import plotly.express as px

st.set_page_config(layout='wide', page_icon='🍁', page_title='NorthDash')

#------dash setup
st.title('Canada Status Dashboard')
st.markdown('Canada by the numbers.')

with st.expander('README', expanded=False):
    st.markdown(
    """
    ### Caveats:
    1. All metrics are reported annually
    2. % change indicators are based on year over year change

    ### Sections:
    1. **TL;DR**: Metric summaries
    2. **Economic Deep Dive**: Detailed economic metrics and breakdowns by industry and province
    3. **Social Deep Dive**: Detailed social metrics and breakdowns by province
    4. **Environmental Deep Dive**: Detailed environmental metrics and breakdowns by province
    """
    )


#-------sidebar setup
st.sidebar.title('🍁 NorthDash')
province = st.sidebar.selectbox(
    'Choose Province', 
    ['Canada', 'Ontario'], 
    help='If you want to see metrics for a specific province instead of all of Canada you can choose which province here.'
)
with st.sidebar.expander('More Parameter Options', expanded=False):
    start_date = st.date_input('Start Date', datetime.date(1900, 1, 1))
    end_date = st.date_input('End Date', datetime.datetime.now())


#-------key metrics
st.header('Section 1: TL;DR')
st.markdown('Metric summaries')

st.subheader('Economic Metrics')
col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.metric('GDP', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col2: 
    st.metric('GDP per Capita', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col3: 
    st.metric('Avg Weekly Earnings', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col4: 
    st.metric('Avg Price', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Social/Environmental Metrics')
col1, col2, col3, col4 = st.columns(4)
with col1: 
    st.metric('Population', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col2: 
    st.metric('% Low Income', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col3: 
    st.metric('% Unemployed', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)
with col4: 
    st.metric('Emissions', value=10, delta='1%')
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada', width=400, height=400)
    st.plotly_chart(fig, use_container_width=True)


#-------drill downs
with st.expander('Section 2: Economic Deep Dive', expanded=False):
    st.header('Section 2: Economic Deep Dive')
    st.markdown('Detailed economic metrics and breakdowns by industry and province')

with st.expander('Section 3: Social Deep Dive', expanded=False):
    st.header('Section 3: Social Deep Dive')
    st.markdown('Detailed social metrics and breakdowns by province')

with st.expander('Section 4: Environmental Deep Dive', expanded=False):
    st.header('Section 4: Environmental Deep Dive')
    st.markdown('Detailed environmental metrics and breakdowns by province')