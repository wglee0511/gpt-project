import streamlit
from langchain.prompts import PromptTemplate 


streamlit.title("Hi")

streamlit.selectbox(label="choose your model", options=("GPT-3", "GPT-4"))