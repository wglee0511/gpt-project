import streamlit

def tab_navigation():
  first_tab, second_tab, third_tab = streamlit.tabs(["첫번쨰", "두번쨰", "세번째"])
  
  with first_tab:
    streamlit.write("1")
    
  with second_tab:
    streamlit.write("2")
    
  with third_tab:
    streamlit.write("3")