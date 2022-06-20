from transformers import pipeline
import pandas as pd


def extractingData(fileName):
    data = pd.read_csv(fileName)
    text = data['Content'][0]

    return text

def test_summarizer(text):
    
    summarizer = pipeline("summarization", model="t5-large")
    output = summarizer(text, max_length=512)

    return output

def strSummary(summary):
    strSummary = summary[0]['summary_text']
    return strSummary

# print(summarizer(extractingData("test.csv")))

def summary_main(fileName):
    text = extractingData(fileName)
    summarized = test_summarizer(text)
    summarized_final = strSummary(summarized)

    return summarized_final

