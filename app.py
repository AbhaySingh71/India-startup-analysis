import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout='wide', page_title='India StartUp Analysis')

@st.cache_data
def load_data():
    df = pd.read_csv('startup_cleaned.csv')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    return df

df = load_data()

def load_overall_analysis():
    st.title('Startup Funding Insights: A Comprehensive Analysis')

    # Total invested amount
    total = round(df['amount'].sum())
    # Max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # Avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()

    # Total funded startups
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric('Total', str(total) + ' cr')

    with col2:
        st.metric('Max', str(max_funding) + ' cr')

    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups', num_startups)

    # 1. Type of Funding Analysis
    st.subheader('Type of Funding')
    funding_type_df = df.groupby('round')['amount'].sum().reset_index().sort_values(by='amount', ascending=False)
    fig1 = px.bar(
        funding_type_df,
        x='round',
        y='amount',
        title='Funding Type Distribution',
        labels={'round': 'Type of Funding', 'amount': 'Total Funding'},
        text='amount'
    )
    fig1.update_layout(
        xaxis_title='Type of Funding',
        yaxis_title='Total Funding',
        xaxis_tickangle=-45,
        yaxis_type='log'
    )
    st.plotly_chart(fig1)


    # 2. City-wise Funding Analysis
    st.subheader('City-wise Funding')
    city_funding_df = df.groupby('city')['amount'].sum().reset_index().sort_values(by='amount', ascending=False)
    fig2 = px.bar(
        city_funding_df,
        x='city',
        y='amount',
        title='City-wise Funding Distribution',
        labels={'city': 'City', 'amount': 'Total Funding'},
        text='amount'
    )
    fig2.update_layout(
        xaxis_title='City',
        yaxis_title='Total Funding',
        xaxis_tickangle=-45,
         yaxis_type='log'
    )
    st.plotly_chart(fig2)

    # 3. Top Startups - Year-wise and Overall
    st.header('Top Startups - Year-wise and Overall')
    year = st.selectbox('Select Year', sorted(df['year'].unique().tolist()))
    top_startups_df = df[df['year'] == year].groupby('startup')['amount'].sum().reset_index().sort_values(by='amount', ascending=False).head(10)
    st.subheader(f'Top Startups of {year}')
    st.table(top_startups_df)

    overall_top_startups_df = df.groupby('startup')['amount'].sum().reset_index().sort_values(by='amount', ascending=False).head(10)
    st.subheader('Top Startups Overall')
    st.table(overall_top_startups_df)

    # 4. Top Investors
    st.header('Top Investors')
    top_investors_df = df['investors'].str.split(',').explode().str.strip().value_counts().reset_index().head(10)
    top_investors_df.columns = ['Investor', 'Number of Investments']
    st.table(top_investors_df)

    # 5. Funding Heatmap
    st.subheader('Funding Heatmap (Year vs. Month)')
    funding_heatmap_df = df.groupby(['year', 'month'])['amount'].sum().unstack().fillna(0)
    fig3 = px.imshow(
        funding_heatmap_df,
        labels=dict(x="Month", y="Year", color="Funding Amount"),
        title='Funding Heatmap',
        color_continuous_scale='blackbody'
    )
    st.plotly_chart(fig3)

     # Sector Analysis Pie Charts
    st.subheader('Sector Analysis')

    # Count of Investments by Sector
    sector_count_df = df['vertical'].value_counts().reset_index()
    sector_count_df.columns = ['Sector', 'Count']
    fig8 = px.pie(
        sector_count_df,
        values='Count',
        names='Sector',
        title='Investments by Sector (Count)',
        labels={'names': 'Sector', 'values': 'Count'}
    )
    st.plotly_chart(fig8)

    # Sum of Funding by Sector
    sector_sum_df = df.groupby('vertical')['amount'].sum().reset_index().sort_values(by='amount', ascending=False)
    fig9 = px.pie(
        sector_sum_df,
        values='amount',
        names='vertical',
        title='Investments by Sector (Sum)',
        labels={'names': 'Sector', 'values': 'Total Funding'}
    )
    st.plotly_chart(fig9)

    # 6. Month on Month Graph
    st.header('Month on Month Graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(
        x=temp_df['x_axis'],
        y=temp_df['amount'],
        mode='lines+markers'
    ))
    fig6.update_layout(
        title='Month-on-Month Analysis',
        xaxis_title='Month-Year',
        yaxis_title='Amount'
    )
    st.plotly_chart(fig6)


def load_investor_details(investor):
    st.title(investor)

    # Load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    # Biggest Investments
    st.subheader('Biggest Investments')
    big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=big_series.index,
        y=big_series.values,
        text=big_series.values,
        textposition='auto'
    ))
    fig1.update_layout(
        title='Biggest Investments',
        xaxis_title='Startup',
        yaxis_title='Total Investment',
        xaxis_tickangle=-45,
        yaxis_type='log'  # Apply logarithmic scale to the y-axis
    )
    st.plotly_chart(fig1)

    # Sectors Invested In
    st.subheader('Sectors Invested In')
    vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
    fig2 = px.pie(
        vertical_series,
        values=vertical_series.values,
        names=vertical_series.index,
        title='Investment by Sector',
        labels={'names': 'Sector', 'values': 'Total Investment'}
    )
    st.plotly_chart(fig2)

    # Year-on-Year Investment
    st.subheader('Year-on-Year Investment')
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=year_series.index,
        y=year_series.values,
        mode='lines+markers',
        name='Yearly Investment'
    ))
    fig3.update_layout(
        title='Year-on-Year Investment',
        xaxis_title='Year',
        yaxis_title='Total Investment',
        yaxis_type='log'  # Apply logarithmic scale to the y-axis
    )
    st.plotly_chart(fig3)

    # Similar Companies
    st.subheader('Similar Companies')
    similar_companies = df[df['vertical'] == df[df['investors'].str.contains(investor)].iloc[0]['vertical']]
    similar_companies = similar_companies[['startup', 'amount']].sort_values(by='amount', ascending=False).head(10)
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        x=similar_companies['startup'],
        y=similar_companies['amount'],
        text=similar_companies['amount'],
        textposition='auto'
    ))
    fig4.update_layout(
        title='Top Similar Companies',
        xaxis_title='Company',
        yaxis_title='Total Investment',
        xaxis_tickangle=-45,
        yaxis_type='log'  # Apply logarithmic scale to the y-axis
    )
    st.plotly_chart(fig4)

    # Stage Pie Chart
    st.subheader('Investment by Stage')
    stage_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
    fig5 = px.pie(
        stage_series,
        values=stage_series.values,
        names=stage_series.index,
        title='Investment by Stage',
        labels={'names': 'Stage', 'values': 'Total Investment'}
    )
    st.plotly_chart(fig5)

    # City Pie Chart
    st.subheader('Investment by City')
    city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
    fig6 = px.pie(
        city_series,
        values=city_series.values,
        names=city_series.index,
        title='Investment by City',
        labels={'names': 'City', 'values': 'Total Investment'}
    )
    st.plotly_chart(fig6)


def load_startup_details(startup):
    st.title(f"Details of {startup}")

    # Filter the data for the selected startup
    startup_data = df[df['startup'] == startup].iloc[0]  # This returns a pandas Series for the first match

    # Display basic company details
    st.subheader('Company Overview')
    st.write(f"**Name:** {startup_data['startup']}")
    st.write(f"**Industry:** {startup_data['vertical']}")
    st.write(f"**Subindustry:** {startup_data['subvertical']}")
    st.write(f"**Location:** {startup_data['city']}")
    st.write(f"**Stage:** {startup_data['round']}")
    st.write(f"**Date:** {startup_data['date'].strftime('%Y-%m-%d')}")

    # Display funding details using DataFrame
    st.subheader('Funding Details')
    funding_info = df[df['startup'] == startup][['date', 'round', 'amount', 'investors']]
    st.table(funding_info)

     # Similar Companies
    st.subheader('Similar Companies')
    similar_companies_df = df[
        (df['vertical'] == startup_data['vertical']) & (df['startup'] != startup)
    ].head(5)
    
    st.write("Companies in the same industry:")
    st.dataframe(similar_companies_df[['startup', 'amount', 'city', 'round']])

    # Funding trends
    st.subheader('Year-on-Year Funding')
    funding_series = df[df['startup'] == startup].groupby('year')['amount'].sum()
    fig, ax = plt.subplots(figsize=(13,7))
    ax.plot(funding_series.index, funding_series.values)
    plt.tight_layout()
    st.pyplot(fig)

    # Investment by funding rounds
    round_series = df[df['startup'] == startup].groupby('round')['amount'].sum()
    st.subheader('Investment by Funding Rounds')
    fig1, ax1 = plt.subplots(figsize=(13,7))
    ax1.bar(round_series.index, round_series.values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig1)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        load_startup_details(selected_startup)
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
