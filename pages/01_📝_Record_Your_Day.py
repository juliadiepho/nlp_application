import streamlit as st
import pandas as pd
import time
from file_writer import ask_input, ask_input_diary, file_writer, info_listing
import csv
import sys

st.set_page_config (
    page_title = "Record Your Day",
    page_icon = "📝"
)

st.header("Record Your Day 📝")

file_name = ask_input_diary()
# st.write(file_name)
if file_name != "" and file_name != None:
    new_file = [file_name]
    diary_list = info_listing("diary_storage.csv")
    if file_name not in diary_list:
        data_content = ask_input(file_name)
        data_header = ["Date", "Content"]
        done = st.button("Done")
        if done:
            # st.write(file_name)
            # st.write(data_content)
            file_writer(file_name, data_content, data_header)
            with st.spinner("Please wait..."):
                time.sleep(1)
            st.success("Your day has been recorded!")
        
            with open("diary_storage.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(new_file)
    else: 
        st.warning("{} already exists. Please choose a different name for your new diary.".format(file_name))