import streamlit as st
import pandas as pd
import numpy as np

st.title(" Streamlit Text Input")

## Create a input text box
name=st.text_input("Enter the name of your's")

if name:
    st.write(f"Hello,{name}!! .Welcome ! To a new Begining")
    
## Create a slider
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}")

## Create a select box or dropdown box
options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose Your favorite language:", options)
st.write(f"You selected {choice}")

df=pd.DataFrame({
    "first_column": [1,2,3,4,5],
    "second_column": [10,12,13,14,15]
})
df.to_csv("sample.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV fiel",type="pdf")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
