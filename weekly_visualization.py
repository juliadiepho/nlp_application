import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from emotion_detector import get_weekly_scores
from PIL import Image

def daily_visualization(emotion, score):
    emotions = pd.read_csv("emotion_recs.csv")
    col1, col2 = st.columns(2)
    # emotions_list = []
    with col1:
        for i in range(len(emotions)):
            if emotion == emotions["Emotion"][i]:
                image = Image.open(emotions["Icon"][i])
                st.image(image, width=200)
                st.text(emotions["Attribute"][i])
    with col2:
        st.subheader("Your dominant emotion of the day is:" + " " + emotion)
        st.write("Score: " + str(score))
    

def weekly_visualization(file_name, text, emotion):
    with open (file_name, "r") as csvfile:
        #read csv file data into data frame
        data = pd.read_csv(file_name, delimiter=",")
        
        data['emotion'] = emotion
        data['emotion score'] = get_weekly_scores(text)
        fig = plt.figure(figsize=(9, 7))
        visualization = sns.barplot(x = "emotion score", y = "emotion", data = data)
        plt.title("Weekly Emotions")
        
        st.pyplot(fig)

