import streamlit
import time
from src.lib.lib import get_page_config

title = "Document-GPT"
get_page_config(title)
streamlit.title(title)

if 'messages' not in streamlit.session_state:
    streamlit.session_state['messages'] = []

  


def send_message(message, role, isSave=True):
  with streamlit.chat_message(role):
    streamlit.write(message)
    if isSave:
      streamlit.session_state["messages"].append({"message": message, "role": role})
    
for message in streamlit.session_state["messages"]:
  send_message(message["message"], message["role"], isSave=False)

chat_input = streamlit.chat_input("AI 에게 메시지를 보내보세요.")

if chat_input:
  send_message(chat_input, "Human")
  time.sleep(2)
  send_message(f"You said: {chat_input}", "AI")
