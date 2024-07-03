import streamlit as st
from src.lib.lib import get_page_config, send_message, paint_massage, get_format_docs
from src.lib.embed import embed_file, ChatCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

if "messages" not in st.session_state:
  st.session_state["messages"] = []

title = "Document-GPT"
get_page_config(title)
st.title(title)
st.subheader("파일을 업로드하고 AI에게 질문하세요")

with st.sidebar:
  file = st.file_uploader(
    label="분석에 사용할 pdf / txt / docx 파일을 업로드 해주세요",
    type=["pdf", "txt", "docx"]
    )

llm = ChatOpenAI(
    temperature=0.1,
    streaming=True,
    callbacks=[ChatCallbackHandler()] 
  )

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 답변 도우미 입니다. 모르는 정보는 지어내지 마세요. 아래 문맥에 따라 답변해 주세요.\n\n {context}"),
    ("human", "{question}")
])

if file:
  retriever = embed_file(file)
  
  send_message("준비가 되었습니다. 질문해 주세요", "AI", False )
  paint_massage()
  
  chat_input = st.chat_input("메시지를 입력해주세요.")
  
  if chat_input:
    send_message(chat_input, "Human")
    chain = {
      "context": retriever | RunnableLambda(get_format_docs),
      "question": RunnablePassthrough()
    } | prompt | llm
    
    with st.chat_message("AI"):
      answer = chain.invoke(chat_input)
  
else:
  st.session_state["messages"] = [ ]