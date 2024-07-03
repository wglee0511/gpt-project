import streamlit as st
from src.lib.lib import get_page_config
from src.lib.embed import embed_file
from langchain.chat_models import ChatOpenAI


title = "Document-GPT"
get_page_config(title)
st.title(title)

file = st.file_uploader(
  label="분석에 사용할 pdf / txt / docx 파일을 업로드 해주세요",
  type=["pdf", "txt", "docx"]
  )

llm = ChatOpenAI(temperature=0.1)

if file:
  retriever = embed_file(file)
  docs = retriever.invoke("김첨지는 어떤 사람인가요")
  st.write(docs)
  