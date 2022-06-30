import csv
import streamlit as st
import pandas as pd
import os

data_header = ["Date", "Content"]

def remove_diary_duplicates(csv_file):
    diaries = pd.read_csv(csv_file)
    # dup_rows = diaries[diaries.duplicated()]
    removed_diaries = diaries.drop_duplicates(keep="first", subset=['Diary Name'])
    # return

def ask_input():
    with st.container():
        date_input = st.date_input("Enter a date")
        user_input = st.text_area("How was your day?")
        data_content = [date_input, user_input]
    
    return data_content

def diary_listing():
    diaries = pd.read_csv("diary_storage.csv")
    diaries = diaries.drop_duplicates(subset=['Diary Name'], ignore_index = True)
        # st.write(diaries)
    diary_list = []

    for i in range (len(diaries)):
        diary_list.append(diaries["Diary Name"][i])
    
    return diary_list

def ask_input_diary():
    ask_file = st.radio("Do you want to create a new diary?", ["Yes", "No"])

    if ask_file == "Yes":
        file_name = st.text_input("Name of your new diary:")
        new_file = [file_name]
        if file_name != "":
            diary_list = diary_listing()
            if file_name not in diary_list:
                with open("diary_storage.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(new_file)
            else:
                st.warning("{} already exists. Please choose a different name for your new diary.".format(file_name))
        elif file_name == "":
            st.error("Please enter a name for your new diary")

    else:
        diary_list = diary_listing()
        file_name = st.selectbox("Choose an existing diary", diary_list)
    
    return file_name

def file_writer (file_name, data_content, data_header):
    with open(file_name, "a") as file:
        writer = csv.writer(file)
        if os.stat(file_name).st_size == 0:
            writer.writerow(data_header)
            writer.writerow(data_content)
        else:
           writer.writerow(data_content) 
           writer = csv.writer(file)
           writer.writerow(data_content)
    # except:
    #     with open(file_name, "w") as file:
    #         data_header = ["Date", "Content"]
    #         writer = csv.writer(file)
    #         writer.writerow(data_header)
    #         writer.writerow(data_content)

# file_writer("test.csv")