import pandas as pandas
import streamlit as streamlit

names_link = 'dataset.csv'

names_data = pd.read_csv(names_link)

st.title('Streamlit con pandas')
st.dataframe(names_data)