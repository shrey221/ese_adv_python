import streamlit as st 
import pandas as pd
def set_theme():
    st.markdown("""
        <style>
            .stApp {
                background-color: black;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
st.markdown("<h1 style='color: #f5c518;'> IMDb Scraped Data Analysis</h1>", unsafe_allow_html=True)
st.image("img.png")
st.markdown("<h4 style='color: white;'> Scraped the data from IMDb Website of title,year,rating,duration</h4>", unsafe_allow_html=True)
st.markdown("https://www.imdb.com/chart/top/")
if st.button("See the scraped dataset"):
    df=pd.read_csv("Final_preprocessed_data.csv")
    st.write(df)
set_theme()
