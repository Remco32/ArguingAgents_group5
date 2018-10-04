import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
import re
from nltk.collocations import TrigramAssocMeasures, TrigramCollocationFinder
#from JSONToCSV import JSONToCSV

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

data = "Medical marijuana shows considerable promise in reducing chronic pain from a widespread number of causes, including cancer, spinal cord injury and disease, severe spasms, post-traumatic stress disorder, nausea, glaucoma, Parkinson's and other debilitating ailments. The drug could prove useful in other applications if patients are allowed to use it.", "\n", "\nIt is nonsensical to oppose the use of medical marijuana in the midst of what amounts to a nationwide epidemic of opioid addiction. Why not provide patients with a safer option? And why continue to allow doctors to prescribe powerful, addictive opiates but deny them the authority to legally prescribe medical marijuana?", "\n", "\nIt is illogical and potentially heartless to deny patients with serious health problems a drug that could help mediate pain and discomfort with few, if any, side effects."



def cleanUp(doc):
    #window_size = 3 #Size of the collocation window


    words = ""
    noLinebreakText = removeLinebreakTags(doc)

    for word in noLinebreakText.split(" "):
        words += " " + word
    translator = str.maketrans('', '', string.punctuation)

    words = words.translate(translator)  # remove punctuation
    tokens = word_tokenize(words)
    words = tokens.copy()
    stop_words = stopwords.words("english")

    words_without_stopwords = [w for w in words if w.lower() not in stop_words and len(w) > 2]  # drop stop_words
    words = [w for w in words_without_stopwords if w.isalpha()]  # keep only words



    output = ""
    for w in words:
        output = output + nltk.stem.WordNetLemmatizer().lemmatize(w, 'v') + " "  # lemmatize verbs

    #TODO find bigrams etc
    output = removeLinebreakTags(output)

    #Clean the text
    #finder = TrigramCollocationFinder.from_words(output, window_size)
    #finder.apply_freq_filter(5) #filter out trigrams with frequency less than 5

    return output

#Removes linebreak tags and returns a single string.
def removeLinebreakTags(doc):
    words = ""
    for word in doc:
        words += re.sub('\\n', "", word) #remove linebreak tags
    return words

#print(cleanUp(data))
#print(removeLinebreakTags(data))

file = open("medicalMarijuana.json", "r") #open test file
content = file.read() #read content

