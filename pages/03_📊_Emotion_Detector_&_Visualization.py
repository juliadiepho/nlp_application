import streamlit as st
import pandas as pd
from emotion_detector import get_emotion_label, get_weekly_emotion, extracting_data_emotion, daily_emotion_detector, weekly_emotion_detector
from weekly_visualization import weekly_visualization, daily_visualization

st.set_page_config (
    page_title = "Emotion Detector & Visualization",
    page_icon = "📊"
)

st.header("Emotion Detector & Summarization 📊")

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True

diaries = pd.read_csv("diary_storage.csv")
diaries = diaries.drop_duplicates(subset=['Diary Name'], ignore_index = True)
diary_list = []

for i in range (len(diaries)):
    diary_list.append(diaries["Diary Name"][i])


file_name = st.selectbox("Choose an existing diary", diary_list, key="emotion") 
option_input = st.radio("Do you want to generate daily or weekly emotion report?", ["Daily", "Weekly"], key="emotion") 
text = extracting_data_emotion(option_input, file_name)

if st.button("Generate Emotion Report") or st.session_state.button_clicked:

    with st.spinner("Please wait..."):
        # emotion = emotion_main(option_input, text)
        if option_input == "Daily":
            emotions = daily_emotion_detector(text)
            emotion = emotions[0]['label']
            score = emotions[0]['score']
            st.success("Success!") 
            # st.write("Your dominant emotion of the day is:", emotion)
            daily_visualization(emotion, score)
            st.balloons()
        else:
            emotions = weekly_emotion_detector(text)
            # st.write("Your emotions throughout the week are:", emotion)
            weekly_visualization(file_name, emotions)
            st.success("Success!") 
            st.balloons()