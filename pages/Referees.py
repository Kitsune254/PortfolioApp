import streamlit as st

st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
    page_title="Selwyn's Portfolio",
    page_icon="💻"
)

st.title("Referees")
st.subheader("1.")
col1, col2 = st.columns([1,5])
with col1:
    st.image("Image_fx (2).jpg")

with col2:
    st.write("Mary Doe")
    st.write("Email Address : marydoe@gmail.com")
    st.write("Phone Number : 00734628791")
    st.write("She has served as a ...")

