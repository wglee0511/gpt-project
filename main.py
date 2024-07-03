import streamlit
from langchain.prompts import PromptTemplate 
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

streamlit.title("Document-GPT")
streamlit.subheader(today)

selected_model = streamlit.selectbox(label="choose your model", options=("GPT-3", "GPT-4"))
if selected_model == "GPT-3":
  streamlit.write("Cheap")
else:
  streamlit.write("Not cheap")
  
selected_temperature = streamlit.slider("민감도를 고르세요", min_value=0.1, max_value=1.0)

streamlit.write("모델명:", selected_model)
streamlit.write("민감도:", selected_temperature )