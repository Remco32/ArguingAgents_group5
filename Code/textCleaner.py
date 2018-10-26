import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
import re

nltk.download('punkt') # Needer for tokenizer
nltk.download('stopwords') # Needed for... stopwords
nltk.download('wordnet') # Needed for lematization

def cleanUp(doc):
    words = ""
    cleanerText = removeLinebreakTags(removeCitations(doc))

    for word in cleanerText.split(" "): #split words
        words += " " + word

    translator = str.maketrans('', '', string.punctuation) #create unicode representation
    words = words.translate(translator)  # remove punctuation

    #Remove stopwords
    tokens = word_tokenize(words) #Tokenize into individual words
    words = tokens.copy()
    stop_words = stopwords.words("english")
    wordsWithoutStopwords = [w for w in words if w.lower() not in stop_words and len(w) > 2]  # drop stopwords
    words = [w for w in wordsWithoutStopwords if w.isalpha()]  # keep only words

    output = ""
    for w in words:
        output = output + nltk.stem.WordNetLemmatizer().lemmatize(w, 'v') + " "  # lemmatize the verbs

    return output

#Removes linebreak tags and returns a single string.
def removeLinebreakTags(doc):
    words = ""
    for word in doc:
        words += re.sub('\\n', "", word) #remove linebreak tags
    return words

#Removes citations for Debatabase output
def removeCitations(doc):
    words = ""
    #CleanUp() takes care of cleaning the citation indicators (i.e. "[3]") from the text already.
    #Look if [1] is in the text
    if(doc.count("[1]") >= 2): #two occurrences, reference and citation
        #look for the second occurrence of [1]
        citationCounter = 0
        for word in doc: #value of count is excluded, so range is [0, count-1]
            words += word #add word to string
            if word == "[1]":
                citationCounter+=1
            if(citationCounter>1):
                break #stop adding words to the string: we reached the citation part
    else:
        words = doc
    return words

#Only removes junk caused by crawling the webpage.
def removeJunk(doc):
    doc = removeLinebreakTags(removeCitations(doc))

    words = ""
    for word in doc.split(" "):
        word = re.sub('\[[0-9]\]', "", word) #remove citation tags
        words += " " + word

    return words