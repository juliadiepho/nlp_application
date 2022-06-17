import string
import pandas as pd

# stop words that can be removed
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

'''
function to clean text: lowercase and remove punctuations
'''
def textTokenizing(fileName): 
    data = pd.read_csv(fileName)
    text = data['Content'][0]
    text = " ".join(text.split())
    lowercasedText = text.lower()
    cleanedText = lowercasedText.translate(str.maketrans("", "", string.punctuation))
    tokenizedText = cleanedText.split()

    return tokenizedText

'''
function to remove stop words from tokenized text
'''
def removeStops(tokenizedText):
    finalText = []
    for word in tokenizedText:
        if word not in stop_words:
            finalText.append(word)
    
    return finalText


print(removeStops(textTokenizing("test.csv")))