import streamlit as st
import pandas as pd
import csv
import time
import seaborn as sns
import matplotlib.pyplot as plt
from file_writer import ask_input, ask_input_diary, file_writer
from summarizer import extracting_data_summary, test_summarizer, str_summary
from emotion_detector import get_emotion_label, get_weekly_emotion, extracting_data_emotion
from weekly_visualization import weekly_visualization

st.title("Welcome to Digital Journal!")
st.markdown("This is where you can write your online dairy, get reports on how you feel daily and weekly, and get summarization of your day and week.")

# ## MAIN FOR STREAMLIT APP

# # Record diary daily expander
# with st.expander("Record your day"):
# # with st.container():
#     file_name = ask_input_diary()
#     # with st.container():
#     if file_name != "" and file_name != None:
#         data_content = ask_input(file_name)
#         if data_content != None:
#             done = st.button("Done")
#             data_header = ["Date", "Content"]
#             if done:
#                 file_writer(file_name, data_content, data_header)
#                 with st.spinner("Please wait..."):
#                     time.sleep(1)
#                 st.success("Your day has been recorded!")


# # Summarization expander
# with st.expander("Summarization"):

#     diaries = pd.read_csv("diary_storage.csv")
#     diaries = diaries.drop_duplicates(subset=['Diary Name'], ignore_index = True)
#     diary_list = []

#     for i in range (len(diaries)):
#         diary_list.append(diaries["Diary Name"][i])

#     file_name = st.selectbox("Choose an existing diary", diary_list, key="summary") 
#     user_input = st.radio("Do you want to generate daily or weekly summarization?", ["Daily", "Weekly"], key="summary")
#     text = extracting_data_summary(user_input, file_name)
#     # st.write(text)

#     summarize = st.button("Generate Summarization")
#     if summarize == True:
#         with st.spinner("Please wait..."):
#             if user_input == "Daily":
#                 summary = str_summary(test_summarizer(text))
#             else:
#                 lst_summary = text.apply(test_summarizer)
#                 summary = lst_summary.apply(str_summary)
#             st.success("Success!") 
#         st.write(summary)


# # Emotion Detector Expander
# with st.expander("Emotion Detector & Visualization"):

#     if "button_clicked" not in st.session_state:
#         st.session_state.button_clicked = False
    
#     def callback():
#         # Button was clicked
#         st.session_state.button_clicked = True
    
#     file_name = st.selectbox("Choose an existing diary", diary_list, key="emotion") 
#     option_input = st.radio("Do you want to generate daily or weekly emotion report?", ["Daily", "Weekly"], key="emotion") 
#     text = extracting_data_emotion(option_input, file_name)

#     if st.button("Generate Emotion Report") or st.session_state.button_clicked:

#         with st.spinner("Please wait..."):
#             # emotion = emotion_main(option_input, text)
#             if option_input == "Daily":
#                 emotion = get_emotion_label(text)
#                 st.success("Success!") 
#                 st.write("Your dominant emotion of the day is:", emotion)
#                 st.balloons()
#             else:
#                 emotion = get_weekly_emotion(text)
#                 st.write("Your emotions throughout the week are:", emotion)
#                 weekly_visualization(file_name, text, emotion)
#                 st.success("Success!") 
#                 st.balloons()
                
#                 # st.write("Your emotions through out the week are:", emotion)

#         # if option_input == "Weekly":
#         #     vis_input = st.radio("Do you want to generate visualization of your week's emotions?", ["Yes", "No"])
#         #     cont_2 = st.button("Continue")  
#         #     callback()          
#         #     if cont_2:
#         #         if vis_input == "Yes":
#         #             weekly_visualization(file_name, text, emotion)
#         #         else:
#         #             st.write("Alright then!")
