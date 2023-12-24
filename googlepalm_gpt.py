import sklearn
import streamlit as st
from langchain.llms import GooglePalm

api_key = 'your api key here'
llm = GooglePalm(google_api_key = api_key, temperature = 0.9)

st.title("Gpt using GooglePalm🌴")
promt = st.text_input("You: ")
if promt:
    response = llm(promt)

    st.header("🤖 BeneGpt")
    st.write(response)
