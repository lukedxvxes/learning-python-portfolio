import streamlit as st

st.set_page_config(layout="wide")

col1, col2, = st.columns(2)

with col1:
    st.image("images/profile.png", width=400)

with col2:
    st.title("Luke Davies")
    content=""" 
        Add something here about a bio
    """
    st.write(content)