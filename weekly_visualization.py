# from numpy import extract
from matplotlib.pyplot import get
import seaborn as sns
# from emotion_detector import extracting_data_emotion
from emotion_detector import get_weekly_scores
import csv
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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

