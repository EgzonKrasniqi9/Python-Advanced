import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name' : ['Egzon','Melina','Lironi','Sata','Reina','Anid'],
    'Age' : [17,17,18,18,16,15],
    'City' : ['Fush Kosove', 'Prishtine','Presheve','Obiliq','Prishtin','Prishtin']

})
st.dataframe(data)
