import streamlit as st
import time


def get_skills(words, speed=0.02):
    container = st.empty()
    displayed_text = ""
    for word in words:
        displayed_text += word + " "
        container.markdown(displayed_text + " ")
        time.sleep(speed)


st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded",
    page_title="Selwyn's Portfolio",
    page_icon="💻"
)

st.title("Selwyn Owoko's Portfolio Website")
dummy1, actual1, dummy2 = st.columns([1, 5, 1])
with actual1:
    st.write("Full-Stack Developer | Android Developer | Python Developer")

st.divider()
col1, col2, col3, col4 = st.columns([1, 5, 5, 1])
with col2:
    st.header("This is Me")
    st.image("selfie.jpg", width=250)

with col3:
    st.header("Get to Know Me")
    st.subheader("General information")
    st.write("Name : Selwyn Owoko")
    st.write("Email : owokoselwyn@gmail.com")
    st.write("Phone Number : 0799266211")
    st.write("Hobbies : Watching Netflix")

st.divider()

skills = [
    "✅ Full Stack Development - HTML, CSS, Javascript, Bootstrap",
    "✅ Android Development - Kotlin",
    "✅ Java Programming Language",
    "✅ Python Programming Language",
    "✅ Data Science"
]


st.header("My Skills")
st.subheader("Click below to know the skills I have acquired")
button = st.button("Click Me!")

if button:
    for skill in skills:
        get_skills(skill)
        time.sleep(0.5)
