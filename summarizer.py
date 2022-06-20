from transformers import pipeline
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer

# # tokenizer = AutoTokenizer.from_pretrained("t5-small")
# summarizer = pipeline("summarization", model="t5-large")
# summaries = {}
# data = pd.read_csv("test.csv")
# text = data['Content'][0]
# # pipe_out = summarizer(text)
# # summaries["t5"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))
# print(data)

def extractingData(fileName):
    data = pd.read_csv(fileName)
    text = data['Content'][0]

def test_summarizer(text):
    
    summarizer = pipeline("summarization", model="t5-large")
    # summaries = {}
    output = summarizer(text, max_length=512)
    # summaries["t5"] = "\n".join(sent_tokenize(pipe_out[0]["summary_text"]))

    return output

def summarizer(text):
    summarizer = pipeline("summarization")
    outputs = summarizer(text, max_length=512, clean_up_tokenization_spaces=True)
    return outputs


def strSummary(summary):
    strSummary = summary[0]['summary_text']
    return strSummary

# print(summarizer(extractingData("test.csv")))
print(strSummary(test_summarizer(extractingData("test.csv"))))
