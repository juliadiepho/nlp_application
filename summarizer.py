from transformers import pipeline
import pandas as pd


def extractingData(fileName):  
    user_input = input("Do you want to generate daily or weekly report? [d/w]: ")
    if user_input == "d": 
        date = input("What is the date that you want to generate report on?: ")
        data = pd.read_csv(fileName)
        for i in range(len(data)):
            if data['Date'][i] == date:
                text = data['Content'][i]
                return text
    elif user_input == "w":
        data = pd.read_csv(fileName)
        text = data['Content'][:7]
        return text
    else:
        return "Please enter a valid input [d/w]"

def test_summarizer(text):
    
    summarizer = pipeline("summarization", model="t5-large")
    output = summarizer(text, max_length=512)

    return output

def str_summary(summary):
    str_summary = summary[0]['summary_text']
    return str_summary

def summary_main(fileName):
    text = extractingData(fileName)
    summarized = test_summarizer(text)
    summarized_final = str_summary(summarized)

    return summarized_final

#print(summary_main("test.csv"))
# print(extractingData("test.csv"))