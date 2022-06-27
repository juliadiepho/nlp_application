import csv
import streamlit as st
import pandas as pd

data_header = ["Date", "Content"]

def ask_input():
    with st.container():
        date_input = st.date_input("Enter a date")
        user_input = st.text_area("How was your day?")
        data_content = [date_input, user_input]
             

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

# file_writer("test.csv")