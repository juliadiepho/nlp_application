# EmoJournal
**EmoJournal** is an online diary web application built with Python and several Natural Language Processing (NLP) models. 

![image](demo_img/home_page.png)
It allows users to input diaries online and get insights of their days and weeks, including daily & weekly summarization and emotional visualization.

## Datasets
1) **Test data** was collected from user WILLOW on https://theopendiaries.com, a public online diary platform.
https://theopendiaries.com/user-diary/61508ca84dab115cc9d1f62d

2) ```emotion_recs.csv``` dataset for Daily Emotion Visualization was created with the 28 emotions used in ```arpanghoshal/EmoRoBERTa``` model with icons from https://www.flaticon.com/ and their attributes.
## Pre-Trained Models

1) **Google's ```t5-large``` model** for summarization task
https://huggingface.co/t5-large
2) **```arpanghoshal/EmoRoBERTa``` model** for emotion detection
https://huggingface.co/arpanghoshal/EmoRoBERTa
