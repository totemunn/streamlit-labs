import pandas as pd
import streamlit as st
import datetime

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data=pd.read_csv(titanic_link)

st.title('Titanic')

sidebar=st.sidebar

sidebar.title('This is the sidebar')
sidebar.write('You can add stuff')

today=datetime.date.today()
today_date=sidebar.date_input('Cual es tu cumple',today)
st.success(f'tu cumple es: {today_date} felicidades!')

st.header('titanic dataset')
agree=sidebar.checkbox('quieres mostrarlo?')

if agree:
    st.dataframe(titanic_data)

st.header('class description')
selected_class=sidebar.radio('select class',titanic_data['class'].unique())

st.success(f'you selected {selected_class}')
st.markdown('___')

selected_sex=sidebar.selectbox('select sex',titanic_data['sex'].unique())

st.success(f'you selected {selected_sex}')
st.markdown('___')

optionals=sidebar.beta_expander('optional configurations',True)
fare_select=optionals.slider(
    'select the fare',
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)

subset_fare=titanic_data[(titanic_data['fare']>= fare_select)]
st.write(f'Number of records w this fare {fare_select}: {subset_fare.shape[0]} ')
st.dataframe(subset_fare)
st.markdown('___')
