import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Marnus Lourens")
    content = """ My name is Marnus Lourens. I am an aspiring software developer. I hold degrees in biochemistry but my
    true passion is writing code to solve problems and minimize tedious repetitive work.
    """
    st.info(content)

text1 = """Below you will be able to find some apps I have been working on
"""
st.write(text1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
