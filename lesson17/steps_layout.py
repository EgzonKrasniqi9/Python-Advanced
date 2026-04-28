import streamlit as st

tab1, tab2, tab3 = st.tabs (["Tab1", "Tab2" , "Tab3" ])

with tab1:
    st.header("The tab 1")
    st.write("This is Tab1")

with tab2:
    st.header("The tab 2")
    st.write("This is Tab2")

with tab3:
    st.header("The tab 3")
    st.write("This is Tab3")
