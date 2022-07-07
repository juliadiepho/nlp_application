from transformers import pipeline
import pandas as pd
import streamlit as st

'''
Function to read a CSV file data into panda DataFrame
@params user's input (Daily/Weekly), csv file name
@return extracted text
'''
def extracting_data_summary(user_input, file_name):  
    if user_input == "Daily": 
        data = pd.read_csv(file_name)
        # Create date list
        date_list = []
        for i in range(len(data)):
            date_list.append(data['Date'][i])
        # Extract data based on date input
        date_option = st.selectbox("Choose a date", date_list, key="s")
        for i in range(len(data)):
            if data['Date'][i] == date_option:
                text = data['Content'][i]
                return text
    # Extract week's data
    elif user_input == "Weekly":
        data = pd.read_csv(file_name)
        text = data['Content'][:7]
        return text

'''
Function to summarize diary data using t5-large
@param extracted text
@return summarized text
'''
def test_summarizer(text):
    # import t5-large
    summarizer = pipeline("summarization", model="t5-large")
    output = summarizer(text, max_length=512)
    return output

'''
Function to extract summarized text as string
@param summarized text
@return summarized text as string
'''
def str_summary(summary):
    str_summary = summary[0]['summary_text']
    return str_summary
