import string

'''
function to clean text: lowercase and remove punctuations
'''
def textCleaning(fileName): 
    text = open(fileName, "r").read()
    text = " ".join(text.split())
    lowercasedText = text.lower()
    cleanedText = lowercasedText.translate(str.maketrans("", "", string.punctuation))

    return cleanedText

#textCleaning("first_test_data.txt")

def tokenizing(cleanedText):
    tokenizedText = cleanedText.split()
    return tokenizedText
