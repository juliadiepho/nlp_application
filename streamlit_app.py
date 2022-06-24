from matplotlib import dates
import streamlit as st
import pandas as pd
import csv
import time
from transformers import pipeline

#from emotion_detector import get_emotion_label, get_weekly_emotion

st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")


def ask_input_diary():
    ask_file = st.radio("Do you want to create a new diary?", ["Yes", "No"])
    
    if ask_file == "Yes":
        file_name = st.text_input("Name of your new diary:")
        if file_name != "":
            with open("diary_storage.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(file_name)
    else:
        diaries = pd.read_csv("diary_storage.csv")
        diary_list = []

        for i in range (len(diaries)):
            diary_list.append(diaries["Diary Name"][i])

        file_name = st.selectbox("Choose an existing diary", diary_list)
    
    return file_name


def ask_input():
    with st.container():
        date_input = st.date_input("Enter a date")
        user_input = st.text_area("How was your day?")
        data_content = [date_input, user_input]
             
        return data_content

data_header = ["Date", "Content"]

def file_writer (file_name, data_content):
    try:
        with open(file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow(data_content)
    except:
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerow(data_header)
            writer.writerow(file_name, data_content)

def extracting_data_emotion(user_input, file_name):  
    #user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"])
    if user_input == "Daily": 
        data = pd.read_csv(file_name)
        date_list = []

        for i in range(len(data)):
            date_list.append(data['Date'][i])
        
        date_option = st.selectbox("Choose a date", date_list, key="e")
        for i in range(len(data)):
            if data['Date'][i] == date_option:
                text = data['Content'][i]
                return text

    elif user_input == "Weekly":
        data = pd.read_csv(file_name)
        text = data['Content'][:6]
        return text
    # else:
    #     return "Please enter a valid input [d/w]"

def extracting_data_summary(user_input, file_name):  
    #user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"])
    if user_input == "Daily": 
        data = pd.read_csv(file_name)
        date_list = []

        for i in range(len(data)):
            date_list.append(data['Date'][i])
        
        date_option = st.selectbox("Choose a date", date_list, key="s")
        for i in range(len(data)):
            if data['Date'][i] == date_option:
                text = data['Content'][i]
                return text

    elif user_input == "Weekly":
        data = pd.read_csv(file_name)
        text = data['Content'][:6]
        return text

def test_summarizer(text):
    summarizer = pipeline("summarization", model="t5-large")
    output = summarizer(text, max_length=512)

    return output

def str_summary(summary):
    str_summary = summary[0]['summary_text']
    return str_summary

def summary_main(fileName):
    text = extracting_data_summary(fileName)
    summarized = test_summarizer(text)
    summarized_final = str_summary(summarized)

    return summarized_final

def daily_emotion_detector(text):
    emotion = pipeline("sentiment-analysis", model="arpanghoshal/EmoRoBERTa")
    emotion_labels = emotion(text)

    return emotion_labels

def get_emotion_label(text):
    return daily_emotion_detector(text)[0]['label']

def get_weekly_emotion(text):
    return (text.apply(get_emotion_label))


## MAIN FOR STREAMLIT APP

# Record diary daily expander
with st.expander("Record your day"):
# with st.container():
    file_name = ask_input_diary()
    data_content = ask_input()

    done = st.button("Done")
    if done == True:
        file_writer(file_name, data_content)
        with st.spinner("Please wait..."):
            time.sleep(3)
        st.success("Your day has been recorded!")

# Summarization expander
with st.expander("Summarization"):

    diaries = pd.read_csv("diary_storage.csv")
    diary_list = []

    for i in range (len(diaries)):
        diary_list.append(diaries["Diary Name"][i])

    file_name = st.selectbox("Choose an existing diary", diary_list, key="summary") 
    user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"], key="summary")
    text = extracting_data_summary(user_input, file_name)
    # st.write(text)

    summarize = st.button("Generate Summarization")
    if summarize == True:
        with st.spinner("Please wait..."):
            if user_input == "Daily":
                summary = str_summary(test_summarizer(text))
            # time.sleep(10)
            else:
                lst_summary = text.apply(test_summarizer)
                summary = lst_summary.apply(str_summary)
            st.success("Success!") 
        st.write(summary)

# Emotion Detector Expander
with st.expander("Emotion Detector"):
    file_name = st.selectbox("Choose an existing diary", diary_list, key="emotion") 
    option_input = st.radio("Do you want to generate daily or weekly emotion report?", ["Daily", "Weekly"], key="emotion") 
    text = extracting_data_emotion(option_input, file_name)

    emo = st.button("Generate Emotion Report")
    if emo == True:
        with st.spinner("Please wait..."):
            if option_input == "Daily":
                emotion = get_emotion_label(text)
                st.success("Success!") 
                st.write("Your dominant emotion of the day is:", emotion)
            else:
                emotion = get_weekly_emotion(text)
                st.success("Success!") 
                st.write("Your emotions through out the week are:", emotion)

                vis_input = st.radio("Do you want to generate visulization of your week's emotions?", ["Yes", "No"])
        