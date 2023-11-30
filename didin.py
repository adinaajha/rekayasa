import streamlit as st
import pandas as pd

def didin():
    df = pd.read_csv("Book1.csv")
    st.subheader("Software enginering")
    st.dataframe(df)
