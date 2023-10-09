import streamlit as st
from functions import *
st.title("YouTube comment scrapper")
link=st.text_input("paste youtube link here:")
data=[]
def fetch_data(link):
    get_data(link,data)
st.button("Fetch",on_click=fetch_data(link))
st.table(data)
# st.dataframe(data,use_container_width=True)