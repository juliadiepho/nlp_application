import csv
# import pandas as pd

data_header = ["Date", "Content"]

def askInput ():
    inputDate = input("The date that you want to write about [M D, Y]: ")
    inputContent = input("How was your day?: ")
    data_content = [inputDate, inputContent]
    
    return data_content

def fileWriter (fileName):
    try:
        with open(fileName, "a") as file:
            writer = csv.writer(file)
            writer.writerow(askInput())
    except:
        with open(fileName, "w") as file:
            writer = csv.writer(file)
            writer.writerow(data_header)
            writer.writerow(askInput())

fileWriter("test.csv")