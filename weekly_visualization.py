import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from emotion_detector import get_weekly_emotion_labels, get_weekly_scores
from PIL import Image
import operator


def daily_visualization(emotion, score):
    emotions = pd.read_csv("emotion_recs.csv")
    col1, col2 = st.columns(2)

    with col1:
        for i in range(len(emotions)):
            if emotion == emotions["Emotion"][i]:
                image = Image.open(emotions["Icon"][i])
                st.image(image, width=200)
                st.text(emotions["Attribute"][i])
    with col2:
        st.subheader("Your dominant emotion of the day is:" + " " + emotion)
        st.write("Score: " + str(score))
    
def weekly_visualization(file_name, emotion):
    with open (file_name, "r") as csvfile:
        #read csv file data into data frame
        data = pd.read_csv(file_name, delimiter=",")
        
        data['emotion'] = get_weekly_emotion_labels(emotion)
        data['emotion score'] = get_weekly_scores(emotion)
        fig = plt.figure(figsize=(9, 7))
        visualization = sns.barplot(x = "emotion score", y = "emotion", data = data)
        plt.title("Weekly Emotions")
        
        st.pyplot(fig)
        return data

def dominant_mood(data):
    sorted_data = sorted(data, key=operator.itemgetter(3), reverse=True)
    dominant = sorted_data['emotion score'][0]

    return dominant

