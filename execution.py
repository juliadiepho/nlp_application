from emotion_detector import emotion_detector
from summarizer import summary_main
from file_writer import fileWriter

fileWriter("test.csv")
text = summary_main("test.csv")
emotion_label = emotion_detector(text)

print("Summary of your day:", text)
print("Your dominant mood of the day:", emotion_label[0]['label'])