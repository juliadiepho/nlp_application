import streamlit as st
from PIL import Image
st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Daily Recording")
    image_1 = Image.open("demo_img/record.png")
    st.image(image_1)
with col2:
    st.subheader("Daily & Weekly Summarization")
    image_2 = Image.open("demo_img/summarize.png")
    st.image(image_2)
with col3:
    st.subheader("Daily & Weekly Emotion Visualization")
    image_3 = Image.open("demo_img/visualization.png")
    st.image(image_3)

