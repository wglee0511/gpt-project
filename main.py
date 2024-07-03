import streamlit
from langchain.prompts import PromptTemplate 
from datetime import datetime
from src.lib.lib import get_page_config

title = "Main"
get_page_config(title)
streamlit.title(title)


streamlit.markdown("""
### GPT-Test Portfolios

  - [ ] [Document-GPT](Document-GPT])
  - [ ] [Private-GPT](Private-GPT])
  - [ ] [Quiz-GPT](Quiz-GPT])
  - [ ] [Site-GPT](Site-GPT])
  - [ ] [Meeting-GPT](Meeting-GPT])
  - [ ] [Investor-GPT](Investor-GPT])

""")