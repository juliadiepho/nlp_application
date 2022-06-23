import streamlit as st
import pandas as pd
import csv
import datetime

st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")


def ask_input_diary():
    ask_file = st.radio("Do you want to create a new diary?", ["Yes", "No"])
    
    if ask_file == "Yes":
        file_name = st.text_input("Name of your new diary:", "")
        # st.write(file_name)
        if file_name != "":
            with open("diary_storage.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(file_name)
    else:
        diaries = pd.read_csv("diary_storage.csv")
        diary_list = []
        for i in range (len(diaries)):
            diary_list.append(diaries["Diary Name"][i])

        file_name = st.multiselect("Choose an existing diary", diary_list)
    
    return file_name


def ask_input():

    date_input = st.date_input("Choose the date that you want to write about")
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


file_name = ask_input_diary()
cont = st.button('Continue')
if cont == True and file_name != []:
    # st.markdown(file_name[0])
    data_content = ask_input()
elif cont == True and file_name == []: 
    st.error("Error: Please select a diary.") 

# done = st.button("Done")
# if done == True:
#     file_writer(file_name, data_content)


# file_name = ask_input_diary()
# st.markdown(file_name[0])
# cont = st.button('Continue')
# if cont == True:
#     data_content = ask_input()
#     file_writer(file_name[0], data_content)

