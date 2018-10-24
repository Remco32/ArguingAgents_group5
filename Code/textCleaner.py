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

data = "The differences between us and other vertebrates are a matter of degree rather than kind.", "[1]", "\u00a0Not only do they closely resemble us anatomically and physiologically, but so too do they behave in ways which seem to convey meaning. They recoil from pain, appear to express fear of a tormentor, and appear to take pleasure in activities; a point clear to anyone who has observed the behaviour of a pet dog on hearing the word \u201cwalk\u201d. Our reasons for believing that our fellow humans are capable of experiencing feelings like ourselves can surely only be that they resemble us both in appearance and behaviour (we cannot read their minds). Thus any animal sharing our anatomical, physiological, and behavioural characteristics is surely likely to have feelings like us. If we accept as true for sake of argument, that all humans have a right not to be harmed, simply by virtue of existing as a being of moral worth, then we must ask what makes animals so different. If animals can feel what we feel, and suffer as we suffer, then to discriminate merely on the arbitrary difference of belonging to a different species, is\u00a0 analogous to discriminating on the basis of any other morally arbitrary characteristic, such as race or sex. If sexual and racial moral discrimination is wrong, then so too is specieism.", "[2]", "\n", "[1]", "\u00a0Clark, S., The Nature of the Beast: are animals moral?, (Oxford : Oxford University Press, 1982)", "\n", "[2]", "\u00a0Singer, P., \u201cAll Animals are Equal\u201d, in La Follette (ed.), Ethics in Practice, (Malden, Mass; Oxford : Blackwell Pub, 2007)", "\n"


def cleanUp(doc):
    # window_size = 3 #Size of the collocation window

    words = ""
    cleanerText = removeLinebreakTags(removeCitations(doc))

    for word in cleanerText.split(" "):
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

    # TODO find n-grams
    output = removeLinebreakTags(output)

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

def removeJunk(doc):
    doc = removeLinebreakTags(removeCitations(doc))

    words = ""
    for word in doc.split(" "):
        word = re.sub('\[[0-9]\]', "", word) #remove citation tags
        words += " " + word

    return words

#print(cleanUp(data))
#print(removeJunk(data))