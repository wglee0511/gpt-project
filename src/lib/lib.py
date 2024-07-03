import streamlit

def get_page_config(title, icon="🌚"):
  streamlit.set_page_config(
    page_title=title, 
    page_icon=icon
  )