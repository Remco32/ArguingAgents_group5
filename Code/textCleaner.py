import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def cleanUp(doc):
    words = ""
    for word in doc:
        words += " " + word
    translator = str.maketrans('', '', string.punctuation)

    words = words.translate(translator) #remove punctuation
    tokens = word_tokenize(words)
    words = tokens.copy()
    stop_words = stopwords.words("english")

    words_without_stopwords = [w for w in words if w.lower() not in stop_words and len(w) > 2] # drop stop_words
    words = [w for w in words_without_stopwords if w.isalpha()] # keep only words

    output = ""
    for w in words:
        output = output + nltk.stem.WordNetLemmatizer().lemmatize(w,'v') + ", " #lemmatize verbs

    return output