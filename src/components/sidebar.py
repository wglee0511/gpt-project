import streamlit

def sidebar(title):
  streamlit.sidebar.title(title)
  
  with streamlit.sidebar:
    streamlit.write("1")
    streamlit.write("2")
  
