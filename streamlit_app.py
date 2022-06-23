import streamlit as st
import pandas as pd
import csv

st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")

def ask_input_diary():
    ask_file = st.radio("Do you want to create a new diary?", ["Yes", "No"])
    if ask_file == "Yes":
        file_name = st.text_input("Name of your new diary:")
        with open("diary_storage.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(file_name)
    else:
        diaries = pd.read_csv("diary_storage.csv")
        diary_list = []
        for i in range (len(diaries)):
            diary_list.append(diaries["Diary Name"][i])

        file_name = st.multiselect("Choose an existing diary", diary_list)
    
    cont = st.button('Continue')
    if cont == True:
        ask_input()
    
    return file_name




def ask_input():
    date_input = st.date_input("Choose the date that you want to write about")
    # st.write(date_input)
    user_input = st.text_area("How was your day?")
    data_content = [date_input, user_input]
    return data_content

# user_input()
data_header = ["Date", "Content"]

def file_writer (file_name):


    try:
        with open(file_name, "a") as file:
            writer = csv.writer(file)
            writer.writerow(ask_input())
    except:
        with open(file_name, "w") as file:
            writer = csv.writer(file)
            writer.writerow(data_header)
            writer.writerow(ask_input())

ask_input_diary()
