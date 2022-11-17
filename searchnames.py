import streamlit as st
import pandas as pd

st.title('Streamlit - Search names')

DATA_URL = ('https://raw.githubusercontent.com/totemunn/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2X2B3NEPF5FWCHPUODDIG4Y3WQKBA')

@st.cache
def load_data_byname(name):
    data=pd.read_csv(DATA_URL)
    filtered_data_byname=data[data['name'].str.contains(name)]
    return filtered_data_byname

myname=st.text_input('Name :')
if (myname):
    filteredbyname=load_data_byname(myname)
    count_row=filteredbyname.shape[0]
    st.write(f'Total names: {count_row}')
    st.dataframe(filteredbyname)