import streamlit as st
import pandas as pd
import numpy as np

## Title of the application

st.title("Hello Streamlit")


## Displaying a simple text
st.write("This is a simple text")

## Create a simple dataframe
df=pd.DataFrame({
    "first_column": [1,2,3,4,5],
    "second_column": [10,12,13,14,15]
})

## Display the dataframe
st.write(" Hey this is the dataframe")
st.write(df)

## Create a line chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)