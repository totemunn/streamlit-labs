import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit con sidebar')

with st.sidebar:
    st.title('Barra')
    st.write('Informacion de mi sidebar')
    check=st.checkbox('show df')

st.header('Hola')

if check == True:
    chart_data=pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c'])
    st.dataframe(chart_data)