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
