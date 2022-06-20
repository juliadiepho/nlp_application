from numpy import extract
from transformers import pipeline
from summarizer import test_summarizer, extractingData, strSummary
import pandas as pd
import nltk


def emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    emotion_labels = emotion(text)

    return emotion_labels

text = strSummary(test_summarizer(extractingData("test.csv")))
print(emotion_detector(text))


# prefix = "summarize: "


# def preprocess_function(fileName):
#     inputs = [prefix + doc for doc in fileName[0]]
#     model_inputs = tokenizer(inputs, max_length=1024, truncation=True)

#     with tokenizer.as_target_tokenizer():
#         labels = tokenizer(fileName["summary"], max_length=128, truncation=True)

#     model_inputs["labels"] = labels["input_ids"]
#     return model_inputs

# print(preprocess_function("test.csv"))

