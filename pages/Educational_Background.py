import streamlit as st

st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
    page_title="Selwyn's Portfolio",
    page_icon="💻"
)

st.title("Educational Background")

st.header("1. Tertiary Education")
with st.expander("University Education"):
    st.write("Kenyatta University")
    st.write("Bachelor of Science (Computer Science)")
    st.write("Status : Ongoing")
    st.write("2024 - Present")

with st.expander("Bootcamps"):
    st.write("eMobilis Technology Training Institute")
    st.write("Course 1 - Full Stack Development & Android Development")
    st.write("Jan 2024 - May 2024")
    st.write("Course 2 - Data Science & Machine Learning")
    st.write("May 2025 - August 2025")

st.header("2. Secondary Education")
with st.expander("Friends School Kamusinga"):
    st.write("Final Grade : A-")
    st.write("2020 - 2023")

st.header("3. Primary Education")
with st.expander("Marell Academy"):
    st.write("Final Marks : 415")
    st.write("2008 - 2019")