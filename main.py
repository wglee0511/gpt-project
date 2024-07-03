import streamlit
from langchain.prompts import PromptTemplate 
from datetime import datetime


streamlit.set_page_config(
  page_title="Document-GPT", 
  page_icon="🌚"
)

streamlit.title("Home")