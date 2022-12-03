import streamlit as st
import pandas as pd
import numpy as np


DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-s ep14.csv.gz'
DATE_COLUMN='Date/Time'

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase=lambda x: str(x).lower()
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    data.rename(lowercase,axis='columns', inplace=True)
    return data

data=load_data(1000)
st.dataframe(data)

st.map(data)
