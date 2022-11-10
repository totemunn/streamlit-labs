import streamlit as st
import pandas as pd

st.title('Streamlit con atributo cache')

DATA_URL='https://raw.githubusercontent.com/totemunn/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2X2B3NAH2UTFGGGNLBX6LAY3NHVNQ'

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state=st.text('Loading data...')
data = load_data(500)
data_load_state.text('Done...')

st.dataframe(data)