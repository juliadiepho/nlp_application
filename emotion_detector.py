from matplotlib.pyplot import get
from numpy import extract
from transformers import pipeline
from summarizer import test_summarizer, extractingData, str_summary
import pandas as pd
# import nltk

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