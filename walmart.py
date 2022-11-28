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

df_selected=df.loc[(df['Discount'] == selected_discount) & 
(df['Ship Mode'] == selected_ship) & 
(df['Category'] == selected_category), 
['Country','Sales']]

fig = px.scatter_geo(df_selected)

st.plotly_chart(fig)