import streamlit as st
import pandas as pd
from summarizer import extracting_data_summary, test_summarizer, str_summary

st.set_page_config (
    page_title = "Summarization ",
    page_icon = "📙"
)

st.header("Summarization 📙")

diaries = pd.read_csv("diary_storage.csv")
diaries = diaries.drop_duplicates(subset=['Diary Name'], ignore_index = True)
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
        else:
            lst_summary = text.apply(test_summarizer)
            summary = lst_summary.apply(str_summary)
        st.success("Success!") 
    st.write(summary)