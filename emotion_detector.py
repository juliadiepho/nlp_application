from matplotlib.pyplot import get
from numpy import extract
from transformers import pipeline
import pandas as pd
import streamlit as st
# from weekly_visualization import weekly_visualization

def extracting_data_emotion(user_input, file_name):  
    #user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"])
    if user_input == "Daily": 
        data = pd.read_csv(file_name)
        date_list = []

        for i in range(len(data)):
            date_list.append(data['Date'][i])
        
        date_option = st.selectbox("Choose a date", date_list, key="e")
        for i in range(len(data)):
            if data['Date'][i] == date_option:
                text = data['Content'][i]
                return text

    elif user_input == "Weekly":
        data = pd.read_csv(file_name)
        text = data['Content'][:7]
        return text

def daily_emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    emotion_labels = emotion(text)

    return emotion_labels

def weekly_emotion_detector(text):
    return text.apply(daily_emotion_detector)

def get_emotion_label(text):
    return daily_emotion_detector(text)[0]['label']

def get_daily_score(text):
    return (daily_emotion_detector(text)[0]['score'])

def get_weekly_scores(text):
    return (text.apply(get_daily_score))

def get_weekly_emotion(text):
    return (text.apply(get_emotion_label))

# def emotion_main(option_input, text, file_name):
#     if option_input == "Daily":
#         emotion = get_emotion_label(text)
#         st.success("Success!") 
#         st.write("Your dominant emotion of the day is:", emotion)
#     else:
#         emotion = get_weekly_emotion(text)
#         weekly_visualization(file_name, text, emotion)
#         st.success("Success!") 
#     return emotion

