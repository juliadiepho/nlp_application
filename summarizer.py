from tensorboard import summary
from transformers import pipeline
import pandas as pd
import csv

def extractingData(fileName):
    date = input("What is the date that you want to generate report on?: ")
    data = pd.read_csv(fileName)
    for i in range(len(data)):
        if data['Date'][i] == date:
            text = data['Content'][i]
            return text
        else:
            return "You have no diaries for {}".format(date)


def test_summarizer(text):
    
    summarizer = pipeline("summarization", model="t5-large")
    # summaries = {}
    output = summarizer(text, max_length=512)
    # summaries["t5"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))

    return output

def strSummary(summary):
    strSummary = summary[0]['summary_text']
    return strSummary

def summary_main(fileName):
    text = extractingData(fileName)
    summarized = test_summarizer(text)
    summarized_final = strSummary(summarized)

    return summarized_final

print(summary_main("test.csv"))
# print(extractingData("test.csv"))