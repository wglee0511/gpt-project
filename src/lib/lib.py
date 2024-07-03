import streamlit as st

def get_page_config(title, icon="🌚"):
  st.set_page_config(
    page_title=title, 
    page_icon=icon
  )
  
def save_massage(message, role):
  st.session_state["messages"].append({"message": message, "role": role})
  
def send_message(message, role, save=True):
  with st.chat_message(role):
    st.markdown(message)
  
  if save:
    save_massage(message, role)
    
def paint_massage():
  for message in st.session_state["messages"]:
    send_message(message["message"], message["role"], False)

def get_format_docs(docs):
  return "\n\n".join(document.page_content for document in docs)