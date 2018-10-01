import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer, word_tokenize


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#data = "Medical marijuana shows considerable promise in reducing chronic pain"


def cleanUp(doc):
    words = ""
    for word in doc.split(" "):
        words += " " + word
    translator = str.maketrans('', '', string.punctuation)

    words = words.translate(translator)  # remove punctuation
    tokens = word_tokenize(words)
    words = tokens.copy()
    stop_words = stopwords.words("english")

    words_without_stopwords = [w for w in words if w.lower() not in stop_words and len(w) > 2]  # drop stop_words
    words = [w for w in words_without_stopwords if w.isalpha()]  # keep only words

    #TODO find bigrams etc
    # Filter out whitespace and symbols with regular expressions
    #tokenizer = RegexpTokenizer(r'\w+')
    #txt = tokenizer.tokenize(words)

    #print(len(txt))
    #print(txt[0:25])

    output = ""
    for w in words:
        output = output + nltk.stem.WordNetLemmatizer().lemmatize(w, 'v') + " "  # lemmatize verbs

    return output


#print(cleanUp(data))
