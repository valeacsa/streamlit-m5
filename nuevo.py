import streamlit as st
import numpy as np 
import pandas as pd 

st.title("streamlit con sidebar")
sidebar = st.sidebar
sidebar.title("Titulo de barra lateral")

sidebar.write("Info de mi sidebar")

st.header("header de mi app")
st.write("Info de mi app")

if st.checkbox("show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randint(1,10, size=(20,3)),
        columns=['col 1', 'col 2', 'col 3'])

    st.dataframe(chart_data)