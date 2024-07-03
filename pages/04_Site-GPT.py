import streamlit
from src.lib.lib import get_page_config

title = "Site-GPT"
get_page_config(title)
streamlit.title(title)
