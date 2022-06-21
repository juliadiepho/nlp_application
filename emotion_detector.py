from numpy import extract
from transformers import pipeline
from summarizer import test_summarizer, extractingData, strSummary
import pandas as pd
import nltk



def daily_emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    emotion_labels = emotion(text)

    return emotion_labels

def weekly_emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    
    return text.apply(emotion)

# text = strSummary(test_summarizer(extractingData("test.csv"))
# print(emotion_detector(text))Date,Content
# text = extractingData("test.csv")
# print(text.apply(emotion))

