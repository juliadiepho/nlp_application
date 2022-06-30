import csv
from datetime import date
from regex import I
import streamlit as st
import pandas as pd
import os

data_header = ["Date", "Content"]

def remove_diary_duplicates(csv_file):
    diaries = pd.read_csv(csv_file)
    # dup_rows = diaries[diaries.duplicated()]
    removed_diaries = diaries.drop_duplicates(keep="first", subset=['Diary Name'])
    # return


def ask_input(file_name):
    with st.container():
        diary = pd.read_csv(file_name)
        date_input = st.date_input("Enter a date")
        date_input_str = str(date_input)

        dates = info_listing(file_name)
        # for i in range(len(diary)):
        if date_input_str in dates:
            st.warning("You already have a record for {}.".format(date_input))
            for i in range(len(diary)):
                if date_input_str == diary['Date'][i]:
                    st.write("Here's what you have for {}:".format(date_input), diary['Content'][i])
            
            data_content = None
            return data_content
                    
            # option = st.radio("Please select an option",["Overwrite", "Add On"])
            # if option == "Overwrite":
            #     user_input = st.text_area("How was your day?",key="overwrite")
            #     diary.replace(diary['Content'][index], user_input)
            #     # data_content = [date_input, diary['Content'][index]]
            #     # return data_content
            # else:
            #     user_input = st.text_area("How was your day?",key="add-on")
            #     diary['Content'] += user_input
            #     data_content = [date_input, diary['Content'][index]]
            #     return data_content
        else:
            user_input = st.text_area("How was your day?",key="none-duplicate")
            data_content = [date_input, user_input]

            return data_content

def info_listing(file_name):
    infos = pd.read_csv(file_name)
    info_list = []
    if file_name == "diary_storage.csv":
        diaries = infos.drop_duplicates(subset=['Diary Name'], ignore_index = True)
        # st.write(diaries)
        # diary_list = []
        for i in range (len(diaries)):
            info_list.append(diaries["Diary Name"][i])
    else:
        for i in range (len(infos)):
            info_list.append(infos["Date"][i])
    
    return info_list

def ask_input_diary():
    ask_file = st.radio("Do you want to create a new diary?", ["Yes", "No"])

    if ask_file == "Yes":
        file_name = st.text_input("Name of your new diary:")
        new_file = [file_name]
        if file_name != "":
            diary_list = info_listing("diary_storage.csv")
            if file_name not in diary_list:
                with open("diary_storage.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(new_file)
            else:
                st.warning("{} already exists. Please choose a different name for your new diary.".format(file_name))
                file_name = None
                return file_name
        elif file_name == "":
            st.error("Please enter a name for your new diary")

    else:
        diary_list = info_listing("diary_storage.csv")
        file_name = st.selectbox("Choose an existing diary", diary_list)
    
    return file_name

def file_writer (file_name, data_content, data_header):
    # if option == None:
        with open(file_name, "a") as file:
            writer = csv.writer(file)
            if os.stat(file_name).st_size == 0:
                writer.writerow(data_header)
                writer.writerow(data_content)
            else:
                writer.writerow(data_content) 
                writer = csv.writer(file)
                writer.writerow(data_content)
