import streamlit as st

st.set_page_config(
    page_title="World Cities MIS",
    page_icon="🌍",
    layout="centered",
)

st.title("Welcome to World Cities MIS 🌍")
st.write(
    "Explore the world’s cities with this interactive Streamlit application."
)

if st.button("Go to the app", type="primary"):
    st.switch_page("pages/app.py")
