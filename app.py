import streamlit as st
import random

st.title("🤖 AI 응원 로봇")
st.write("힘든 일이 있나요? 제가 응원해 드릴게요!")
user_input = st.text_input("여기에 문장을 입력하세요:", "공부가 힘들어")

if st.button("응원 받기"):
    st.balloons()
    cheers = ["당신은 할 수 있어요!", "오늘 정말 고생 많았어요.", "천천히 가도 괜찮아요."]
    st.success(random.choice(cheers))
