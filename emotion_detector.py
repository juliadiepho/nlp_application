from matplotlib.pyplot import get
from numpy import extract
from transformers import pipeline
import pandas as pd
import streamlit as st
# from weekly_visualization import weekly_visualization

'''
Is this the same with extracting_data from summarizer?
'''
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

'''
Daily emotion detector usng EmoRoBERTa
@param extracted content from a specific date
@return emotion label with score
'''
def daily_emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    emotion_labels = emotion(text)

    return emotion_labels

'''
Weekly emotion detector 
@param extracted content of the week
@return emotion labels with scores
'''
def weekly_emotion_detector(text):
    return text.apply(daily_emotion_detector)

'''
Daily emotion label getter
@param extracted daily text
@return emotion label as string
'''
def get_emotion_label(emotions):
    return emotions[0]['label']

'''
Weekly emotion labels getter
@param extracted daily text
@return emotion label as string
'''
def get_weekly_emotion_labels(emotions):
    return emotions.apply(get_emotion_label)
    
'''
Daily emotion score getter
@param extracted daily text
@return 
'''
def get_daily_score(emotions):
    return (emotions[0]['score'])

def get_weekly_scores(emotions):
    return (emotions.apply(get_daily_score))

def get_weekly_emotion(text):
    return (text.apply(daily_emotion_detector))


