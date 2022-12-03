import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Walmart USA Dashboard')
st.sidebar.caption('Click the sliders to control the graphs')
st.write('This dashboard intends to show the sales prediction of the clothing line in USA Walmart branches.')


df=pd.read_csv('Global Superstore Orders.csv')
selected_ship=st.sidebar.radio('Select ship mode',df['Ship Mode'].unique())

selected_category=st.sidebar.selectbox('Select the category',df['Category'].unique())

optionals=st.sidebar.expander('Optional configurations',True)
selected_discount=optionals.slider('Select the discount percentage',
min_value=float(df['Discount'].min()),
max_value=float(df['Discount'].max()))

df_selected=df.loc[(df['Discount'] == selected_discount)]
df_selected=df_selected.loc[(df_selected['Ship Mode'] == selected_ship)]
df_selected=df_selected.loc[(df_selected['Category'] == selected_category)]


df3 = pd.read_csv('country-and-continent-codes-list.csv')
df3=df3.drop(['Continent_Code','Two_Letter_Country_Code','Country_Number'],axis=1)

df_map = df_selected.merge(df3, how = 'inner', left_on = 'Country', right_on = 'Country_Name')
#df_map = df_selected.drop(['Country_Name'],axis=1)
df_map.rename(columns = {'Continent_Name':'continent'}, inplace = True)

fig = px.scatter_geo(df_map,locations="Three_Letter_Country_Code")

fig_hist = px.histogram(df_selected, x="Quantity")

fig_bar = px.bar(df_selected, x='Segment', y='Sub-Category')

fig_pie = px.pie(df_selected, values='Segment', names='Region')

st.plotly_chart(fig)
st.plotly_chart(fig_hist)
st.plotly_chart(fig_bar)
st.plotly_chart(fig_pie)
