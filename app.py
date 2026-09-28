# EduGenie AI - Personal AI Learning Buddy
import streamlit as st

st.set_page_config(page_title="EduGenie AI", page_icon="🎓")

st.title("🎓 EduGenie AI - Your Personal Learning Buddy")
st.write("Ask any doubt, I will explain simply!")

subject = st.selectbox("Choose Subject:", ["Maths", "Science", "Computer Science", "History"])

question = st.text_input("Un Doubt Enna?")

if st.button("Ask EduGenie"):
    if question:
        st.success(f"**EduGenie Answer:**")
        st.write(f"Your question about '{question}' in {subject} is very good!")
        st.write("Here is a simple explanation: This topic is about basics. If you study 30 mins daily, you will become expert!")
        st.write("💡 Tip: Revise daily and ask doubts!")
    else:
        st.warning("Please type your doubt da!")

st.sidebar.title("About")
st.sidebar.info("Created by Yuthra | Final Year Project")
