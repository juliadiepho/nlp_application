
from transformers import pipeline
import pandas as pd


def extractingData(fileName):  
    date = input("What is the date that you want to generate report on?: ")
    data = pd.read_csv(fileName)
    for i in range(len(data)):
        if data['Date'][i] == date:
            text = data['Content'][i]
            return text

def test_summarizer(text):
    
    summarizer = pipeline("summarization", model="t5-large")
    output = summarizer(text, max_length=512)

    return output

def strSummary(summary):
    strSummary = summary[0]['summary_text']
    return strSummary


def summary_main(fileName):
    text = extractingData(fileName)
    summarized = test_summarizer(text)
    summarized_final = strSummary(summarized)

    return summarized_final

