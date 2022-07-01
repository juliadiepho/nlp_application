import streamlit as st
import pandas as pd
import time
from file_writer import ask_input, ask_input_diary, file_writer


# with st.expander("Record your day"):
# with st.container():
st.header("Record Your Day")

file_name = ask_input_diary()
# with st.container():
if file_name != "" and file_name != None:
    data_content = ask_input(file_name)
    if data_content != None:
        done = st.button("Done")
        data_header = ["Date", "Content"]
        if done:
            file_writer(file_name, data_content, data_header)
            with st.spinner("Please wait..."):
                time.sleep(1)
            st.success("Your day has been recorded!")