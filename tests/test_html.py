import streamlit as st

st.set_page_config(layout="wide")

html = """
<div style="
background:red;
padding:30px;
color:white;
font-size:30px;
border-radius:10px;
">
Hello World
</div>
"""

st.markdown(html, unsafe_allow_html=True)