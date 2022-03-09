#Import de Bibliotecas
import geopandas
import pandas as    pd
import streamlit as st
import numpy as np
import folium
import plotly.express as px

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

#Page config
st.set_page_config(
    page_title='Real Estate Company',
    layout='wide')

#get data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data

path = 'kc_house_data2.csv'
df = get_data(path)

st.title('Real Estate Company Portfolio')

st.header('1. Premises Adopted and Solution Plan')
st.subheader('1.1 Premises Adopted')
st.write('This project has the objective to help the Real Estate Company to find good home buying opportunities and'
         ' inform the bussiness team the potential opportunities making it possible to ressell at higher prices obtaining' 
         ' profit considering the best moment to resell')
st.write('1. Which properties we should buy and how much to sell?')
st.write('2. When is the best time to buy/sell properties?')
st.write('So, the data product below has the objective to answer these questions, and also to produce other relevant '
        'insights that may be able to have an impact in decision-making and, consequently, in the business itself.')

st.subheader('1.2 Solution Plan')

st.write('The solution plan can be understood with the following points:')
st.write('- Identify good buying opportunites: In this part, my objective with data manipulation was find the median price of properties with the same attributes,'
'these attributes, which are more impacting on the price:'
' zipcode, condition, sqft_lot_level, price. When the property is priced lower than properties with the same characteristics, then this propertie'
' is considered a buying opportunity. Excellent offers are properties with condition equal or more than 4; Good Offers are properties with condition between 2 and 3. If the price'
' was attractive but the condition attribute was equal to 1: not recommended buying' ) 

st.write('- Best time for resale: As we can see below, the best moment to sell properties is the spring season and the best moment to buy these properties'
'is in the winter season:')

df_aux = df[['price', 'season']].groupby('season').median().reset_index()
df_aux.columns = ['Season', 'Median Price']

st.dataframe(df_aux)

st.write("- Margin of profit to be able to sell: In this part, the profit's percentages varies according to the season:")
st.write('If Winter: Sell Price = Buy Price * 1.07 (7% of profit)')
st.write('If Autumn: Sell Price = Buy Price * 1.12 (12% of profit)')
st.write('If Summer: Sell Price = Buy Price * 1.15 (15% of profit)')
st.write('If Spring: Sell Price = Buy Price * 1.20 (20% of profit)') 

st.header('2.0 Validation of hypothesis - Insights Obtained')
c1, c2 = st.columns( (1, 1) ) #wrap of the h1 and h2
c3, c4 = st.columns( (1, 1) ) #wrap of the h3 and h4

#Hipoteshis 1 (waterview):

with c1:
    
    dfh1 = df[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
    st.write('H1: Properties with waterview, are on avarage, more expensive. (True)')
    fig1 = px.bar(dfh1, x='waterfront', y='price', labels= {'waterfront': 'Propreties with WaterView, 0 no; 1 yes', 'price': 'Mean Price'}, 
                  color='price', color_discrete_sequence=px.colors.qualitative.Vivid, title='Mean Price - WaterView x No Water View')
    st.plotly_chart(fig1)
    st.write('As we can see below, properties with waterview are, on average, 193,1% more expensive.')

#Hipoteshis 2 (houses before 1955):

with c2:
    df_grouped_before_1955 = df.loc[df['yr_built'] <= '1955-01-01', ['price', 'yr_built']].groupby(by='yr_built').mean().reset_index()
    df_grouped_after_1955 = df.loc[df['yr_built'] > '1955-01-01', ['price', 'yr_built']].groupby(by='yr_built').mean().reset_index()

    dict = {'Before/After 1955': ['Before 1955', 'After 1955'], 'Mean Price': [df_grouped_before_1955['price'].mean(), df_grouped_after_1955['price'].mean()]}
    dfh2 = pd.DataFrame(data=dict)

    st.write('H2: Properties built before 1955 are on average 15% cheaper. (False)')
    fig2= px.bar(dfh2, x='Before/After 1955', y='Mean Price', color = 'Mean Price', color_discrete_sequence=px.colors.qualitative.Vivid,
     title='Mean Price - Before 1955 x After 1955')
    st.plotly_chart(fig2)
    st.write('As we can see below, properties built before 1955 are actually 4.11% more expensive than properties built after 1955')


#Hipoteshis 3 (Basement-Renovated):

with c3:

    num_houses_with_basement_withrenovation = len(df.loc[(df['sqft_basement'] !=0) & (df['yr_renovated'] != '1900-01-01')])
    num_houses_with_basement_withoutrenovation = len(df.loc[(df['sqft_basement'] !=0) & (df['yr_renovated'] == '1900-01-01')])
    total_houses_with_basement = num_houses_with_basement_withrenovation + num_houses_with_basement_withoutrenovation
    dict = {'Properties With Basement': ['Basement', 'Basement'], 
            'Type': ['withrenovation', 'withoutrenovation'], 'Count': [num_houses_with_basement_withoutrenovation, num_houses_with_basement_withrenovation]}
    dfh3 = pd.DataFrame(data=dict)

    st.write('H3: 30% of properties with a basement have been renovated at least once. (False)')
    fig3= px.bar(dfh3, x='Properties With Basement', y='Count', color='Type', color_discrete_sequence=['yellow', 'blue'],
                 title='Proportion of Renovation - Houses With Basement')
    st.plotly_chart(fig3)
    st.write('In fact, 5.47% of properties with a basement have been renovated at least once.')

#Hipoteshis 4 (Floors Distributions):

with c4:
    
    st.write('H4: In terms of "floors", the most common type of properties are those with 1.0 floors. (True)')
    fig4= px.histogram(df, x='floors', color_discrete_sequence=['yellow'], title='Distribution of Attribute Floors')
    st.plotly_chart(fig4)
    st.write('As we can see in the histogram above, the most common type of properties are those that have 1.0 floors')


#get geofile
@st.cache(allow_output_mutation=True)
def get_geofile( url ):
    geofile = geopandas.read_file( url )
    return geofile

url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
geofile = get_geofile(url)

# Portfolio Density 

st.title('3.0 Region Overview - Properties Indicated as Opportunity to Buy')

st.subheader('Porfolio Table Exploration (filter on left side the recommendation column)')

df2 = df.copy()
f_recommendation = st.sidebar.multiselect('Filter the type of buy recommendation', options = df2['recommendation'].unique().tolist())

if (f_recommendation != []):
    df2 = df2.loc[df2['recommendation'].isin(f_recommendation), :]
elif (f_recommendation == []):
    df2 = df2

st.dataframe(df2, height=300)

st.subheader('Properties Classified as Opportunites - Map')

df4 = df[(df['recommendation'] == 'buy - excellent') | (df['recommendation'] == 'buy - good')]

st.write('H5: The buying reccomendations properties are found mostly in East Seattle. (False)')

portfolio_density = folium.Map(
    location=[df4['lat'].mean(), df4['long'].mean()],
    default_zoom_start=15, 
    width=1500, 
    height=500)

marker_cluster = MarkerCluster().add_to(portfolio_density)
for i, row in df4.iterrows():
    if (row['recommendation'] == 'buy - excellent'):
        folium.Marker( [row['lat'], row['long'] ], icon = folium.Icon(color='green', icon_color='green'), popup='Price ${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}, recommendation: {6}'.format( 
        row['price'],
        row['date'],
        row['sqft_living'],
        row['bedrooms'],
        row['bathrooms'],
        row['yr_built'],
        row['recommendation'])).add_to(marker_cluster)

    elif (row['recommendation'] == 'buy - good'):
        folium.Marker( [row['lat'], row['long'] ], icon = folium.Icon(color='blue', icon_color='blue'), popup='Price ${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}, recommendation: {6}'.format(
        row['price'],
        row['date'],
        row['sqft_living'],
        row['bedrooms'],
        row['bathrooms'],
        row['yr_built'],
        row['recommendation'])).add_to(marker_cluster)

folium_static(portfolio_density, width=1200)

st.write('Actually, the buying reccomendations properties are found mostly in North Seattle.')

# Price Density

st.subheader("Price Density (all properties)")

st.write('H6: The north has the highest priced houses. (False)')

df5 = df[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
df5.columns = ['ZIP', 'PRICE']

geofile = geofile[geofile['ZIP'].isin( df5['ZIP'].tolist() )]

region_price_map = folium.Map(
    location= [df['lat'].mean(), df['long'].mean()],
    default_zoom_start=15 )

region_price_map.choropleth(
    data=df5,
    geo_data = geofile,
    columns=['ZIP', 'PRICE'],
    key_on='feature.properties.ZIP',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='AVG PRICE'
)

folium_static(region_price_map, width= 1200)

st.write('Actually the east region has the highest priced houses.')

st.header('4.0 Studies of Growth')
c5, c6 = st.columns( (1, 1) ) #wrap of the h7 and h8

with c5:
    st.write('H7: The annual growth in house prices is around 5% (False).')
    df6 = df.copy()
    df6['date'] = pd.to_datetime(df6['date']).dt.strftime('%Y')
    dfh8 = df6[['date', 'price']].groupby('date').mean().reset_index()
    fig5 = px.line(dfh8, x='date', y='price', labels={'date': 'Time', 'price': 'Median Price'}, title='Median Prices per Year')
    st.plotly_chart(fig5)
    st.write('The graph above shows that the growth from 2014 to 2015 was around 0.11%, thus devaluing the hypothesis.')

with c6:
    st.write('H8: The monthly house price growth is somewhat linear, always maintaining price stability (False).')
    dfh7 = df[['date', 'price']].groupby('date').mean().reset_index()
    fig6 = px.line(dfh7, x='date', y='price', labels={'date': 'Time', 'price': 'Median Price'}, title='Median Prices per Month')
    st.plotly_chart(fig6)
    st.write('The graph above shows that the growth in house prices showed stable trends, decreasing and increasing at the same pace')

st.write('H9: Houses before 1960 have a lower average price (False).')
df7 = df.copy()
df7['yr_built'] = pd.to_datetime(df7['yr_built']).dt.strftime('%Y')
dfh8 = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()
fig7 = px.line(dfh8, x='yr_built', y='price', labels={'date': 'Year Built', 'price': 'Median Price'}, title='Median Prices per Year Built')
st.plotly_chart(fig7, use_container_width=True)
st.write('H9: The graph above shows that houses builted before 1960 have median prices equivalent to houses builted after 1960')

st.subheader('5.0 Financial Results')
st.write('If the company follows the strategy here described and buy the properties classified as buy opportunites,'
         ' it is estimated that the annual profit around $ 400.896.000 (not included taxes), I believe it is possible to see an increase'
         ' of about 15% ingross revenue.')
st.subheader('6.0 Projects Improvement - Next Steps')
st.write('I suggest a implementation of a machine learning algorithm in order to help the company Real Estate Company make these analyzes and '
         'predictions faster. I reinforce that it is important to receive feedback from bussiness team which will consume this data product. '
         "I reiterate the importance of keeping the database accurate and up-to-date to maintain strategy's accuracy, turning possible to keep indicating good buying opportunities.")
st.subheader('7.0 Conclusions')
st.write('With the help of this data product, the Real Estate Company will be able to gain productivity and address interesting purchase offers '
          'and make sales that are advantageous for it. I believe that the insights generated in the analysis will help the bussiness team open your '
          'mind to create new profit strategies.')