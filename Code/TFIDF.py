# The TF.IDF calculation gives each unique word in a given text a value representing the word's relevance compared to
# other values in a set of documents. In our project, this means we can find values that represent any given argument.
#
# We can later test these values against dictionaries with common "positive" and "negative" words to try and find whether
# an argument is "pro" or "con".

import math
import operator
import os
import pandas as pd

from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from collections import Counter
from topic import Argument

# Create a representation of a given corpus for a single document
def TFIDFRep(corpus, doc):
    term_counts = Counter(corpus.words(doc))
    #print('TF.DIF values of words in ' + doc)
    rep = dict()
    #Calculate TFIDF values
    for term in term_counts:
        value = TFIDF(term, doc, corpus, term_counts)
        rep[term] = value
    # sort the found TF.IDF values
    rep = rankValues(rep)
    #print(rep)
    return rep

# Calculate the TF.IDF value
def TFIDF(term, doc, docs, term_counts):
    words = docs.words(doc)
    return TF(term, words, term_counts) * IDF(term, docs)

# Calculate the TF
def TF(term, words, term_counts):
    total_no_terms = len(words)
    count = term_counts[term]
    return math.log(count / total_no_terms)

# Calculate the IDF
def IDF(term, docs):
    n = len(docs.fileids())
    return math.log((n+1)/(DF(term, docs)+1))+1

# Calculate the DF
def DF(term, docs):
    docs_counts = 0
    for doc in docs.fileids():
        if term in docs.words(doc):
            docs_counts = docs_counts + 1
    return docs_counts

# Sort the TF.IDF values from top to bottom
def rankValues(values):
    return sorted(values.items(), key=operator.itemgetter(1))

# Create corpus from text files
def corpusize(filepath):
    if filepath[-1] != '/':
        filepath = filepath + '/'

    os.chdir('..')
    return PlaintextCorpusReader(filepath, '.*')

# Create a confusion matrix for this corpus
def confMatrix(predArray, corpus):
    actuArray = list()

    for doc in corpus.fileids():
        if "pro" in doc:
            actuArray.append("pro")
        elif "con" in doc:
            actuArray.append("con")

    df_confusion = pd.crosstab(pd.Series(actuArray, name="Actual"), pd.Series(predArray, name="Predicted"))

    # Compute accuracy


    print(df_confusion)

def test(filepath):
    corpus = corpusize(filepath)
    values = dict()
    for doc in corpus.fileids():
        values[doc] = TFIDFRep(corpus, doc)
    proconcorpus = corpusize("../Resources/Opinion Lexicon/Trimmed/")

    proDocs = list()
    conDocs = list()
    nulDocs = list()

    predArray = list()

    for doc in values.keys():
        docValues = values[doc]
        proVal = 0
        conVal = 0
        for tuple in docValues:
            word = tuple[0]
            if word in proconcorpus.words("positive-words-trimmed.txt"):
                proVal += tuple[1]
            elif word in proconcorpus.words("negative-words-trimmed.txt"):
                conVal += tuple[1]
        if proVal < conVal:
            proDocs.append(doc)
            predArray.append("pro")
        elif proVal > conVal:
            conDocs.append(doc)
            predArray.append("con")
        else:
            nulDocs.append(doc)
            predArray.append("???")

    print("Pro arguments:", proDocs)
    print("Con arguments:", conDocs)
    print("Unable to determine:", nulDocs)

    confMatrix(predArray, corpus)


def classify_argument(argument, test_topic):
    topicpath = '../Crawler/Corpus/' + test_topic + '/'

    # Create a file for the argument in the correct folder
    argumentFile = open(topicpath + 'input.txt', "w+")
    argumentFile.write(argument)
    argumentFile.close()

    corpus = corpusize(topicpath)
    values = dict()
    for doc in corpus.fileids():
        values[doc] = TFIDFRep(corpus, doc)
    proconcorpus = corpusize("../Resources/Opinion Lexicon/Trimmed/")

    proDocs = list()
    conDocs = list()
    nulDocs = list()

    predArray = list()

    for doc in values.keys():
        docValues = values[doc]
        proVal = 0
        conVal = 0
        for tuple in docValues:
            word = tuple[0]
            if word in proconcorpus.words("positive-words-trimmed.txt"):
                proVal += tuple[1]
            elif word in proconcorpus.words("negative-words-trimmed.txt"):
                conVal += tuple[1]
        if proVal < conVal:
            proDocs.append(doc)
            predArray.append("pro")
        elif proVal > conVal:
            conDocs.append(doc)
            predArray.append("con")
        else:
            nulDocs.append(doc)
            predArray.append("???")

    if values[argumentFile] in proDocs:
        return Argument.PRO
    else:
        return Argument.CON


test('Crawler/Corpus/ProconOrg/longArguments/medicalMarijuana')