# from matplotlib import dates
import streamlit as st
import pandas as pd
import csv
import time
# from transformers import pipeline
import seaborn as sns
import matplotlib.pyplot as plt
from file_writer import ask_input, ask_input_diary, file_writer
from summarizer import extracting_data_summary, test_summarizer, str_summary
from emotion_detector import get_daily_score, get_emotion_label, get_weekly_emotion, get_weekly_scores, extracting_data_emotion

st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")

def weekly_visualization(file_name, text, emotion):
    with open (file_name, "r") as csvfile:
        data = pd.read_csv(file_name, delimiter=",")
        # text = extractingData(file_name)
        data['emotion'] = emotion
        data['emotion score'] = get_weekly_scores(text)
        fig = plt.figure(figsize=(9, 7))
        visualization = sns.barplot(x = "emotion score", y = "emotion", data = data)
        plt.title("Weekly Emotions")
        
        st.pyplot(fig)
        # return visualization

## MAIN FOR STREAMLIT APP

# Record diary daily expander
with st.expander("Record your day"):
# with st.container():
    file_name = ask_input_diary()
    data_content = ask_input()

    done = st.button("Done")
    if done == True:
        file_writer(file_name, data_content)
        with st.spinner("Please wait..."):
            time.sleep(3)
        st.success("Your day has been recorded!")

# Summarization expander
with st.expander("Summarization"):

    diaries = pd.read_csv("diary_storage.csv")
    diary_list = []

    for i in range (len(diaries)):
        diary_list.append(diaries["Diary Name"][i])

    file_name = st.selectbox("Choose an existing diary", diary_list, key="summary") 
    user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"], key="summary")
    text = extracting_data_summary(user_input, file_name)
    # st.write(text)

    summarize = st.button("Generate Summarization")
    if summarize == True:
        with st.spinner("Please wait..."):
            if user_input == "Daily":
                summary = str_summary(test_summarizer(text))
            # time.sleep(10)
            else:
                lst_summary = text.apply(test_summarizer)
                summary = lst_summary.apply(str_summary)
            st.success("Success!") 
        st.write(summary)

# Session State
# if 'count' not in st.session_state:
#     st.session_state = 0
# def increment_counter():
#     st.session_state.count += 1

# Emotion Detector Expander
with st.expander("Emotion Detector & Visualization"):
    file_name = st.selectbox("Choose an existing diary", diary_list, key="emotion") 
    option_input = st.radio("Do you want to generate daily or weekly emotion report?", ["Daily", "Weekly"], key="emotion") 
    text = extracting_data_emotion(option_input, file_name)

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False
    
    def callback():
        # Button was clicked
        st.session_state.button_clicked = True

    if st.button("Generate Emotion Report", on_click=callback) or st.session_state.button_clicked:
        # st.session_state.count += 1
        with st.spinner("Please wait..."):
            if option_input == "Daily":
                emotion = get_emotion_label(text)
                st.success("Success!") 
                st.write("Your dominant emotion of the day is:", emotion)
            else:
                emotion = get_weekly_emotion(text)
                st.success("Success!") 
                st.write("Your emotions through out the week are:", emotion)

                vis_input = st.radio("Do you want to generate visualization of your week's emotions?", ["Yes", "No"])
                # callback()
                cont_2 = st.button("Continue")            
                if cont_2:
                    if vis_input == "Yes":
                        weekly_visualization(file_name, text, emotion)
                    else:
                        st.write("Alright then!")
