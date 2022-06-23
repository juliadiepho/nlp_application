import csv
# import pandas as pd

data_header = ["Date", "Content"]

def ask_input ():
    input_date = input("The date that you want to write about [M D, Y]: ")
    input_content = input("How was your day?: ")
    data_content = [input_date, input_content]
    
    return data_content

def file_writer (fileName):
    try:
        with open(fileName, "a") as file:
            writer = csv.writer(file)
            writer.writerow(ask_input())
    except:
        with open(fileName, "w") as file:
            writer = csv.writer(file)
            writer.writerow(data_header)
            writer.writerow(ask_input())

file_writer("test.csv")