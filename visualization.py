# from numpy import extract
from matplotlib.pyplot import get
import seaborn as sns
from summarizer import extractingData
from emotion_detector import get_weekly_emotion, weekly_emotion_detector, get_weekly_scores
import csv
import pandas as pd
import matplotlib.pyplot as plt

def weekly_visualization(file_name):
    with open (file_name, "r") as csvfile:
        data = pd.read_csv(file_name, delimiter=",")
        text = extractingData(file_name)
        data['emotion'] = get_weekly_emotion(text)
        data['emotion score'] = get_weekly_scores(text)
        visualization = sns.barplot(x = "emotion score", y = "emotion", data = data)
        # print(data)
        # sns.countplot(data = data, y = 'emotion').set_title('Emotion Distribution')
        plt.show()

weekly_visualization("test.csv")
