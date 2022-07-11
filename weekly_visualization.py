import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from emotion_detector import get_weekly_emotion_labels, get_weekly_scores
from PIL import Image

'''
Function to perform daily emotion visualization
@params emotion_label, score
'''
def daily_visualization(emotion_label, score):
    # read emotion database
    emotions = pd.read_csv("emotion_recs.csv")
    col1, col2 = st.columns(2)

    with col1:
        for i in range(len(emotions)):
            if emotion_label == emotions["Emotion"][i]:
                # corresponding image with the emotion
                image = Image.open(emotions["Icon"][i])
                st.image(image, width=200)
                st.text(emotions["Attribute"][i])
    with col2:
        st.subheader("Your dominant emotion of the day is:" + " " + emotion_label)
        st.write("Score: " + str(score))
    
'''
Function to perform weekly emotion visualization with bar graph
@params file_name, emotions
'''
def weekly_visualization(file_name, emotions):
    with open (file_name, "r") as csvfile:
        #read csv file data into data frame
        data = pd.read_csv(file_name, delimiter=",")
        # add emotions and scores to data frame
        data['emotion'] = get_weekly_emotion_labels(emotions)
        data['emotion score'] = get_weekly_scores(emotions)
        fig = plt.figure(figsize=(9, 7))
        visualization = sns.barplot(x = "emotion score", y = "emotion", data = data)
        plt.title("Weekly Emotions")
        
        st.pyplot(fig)

# def dominant_mood(data):
#     sorted_data = sorted(data, key=operator.itemgetter(3), reverse=True)
#     dominant = sorted_data['emotion score'][0]

#     return dominant

