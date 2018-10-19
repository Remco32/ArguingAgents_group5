from enum import Enum
from textCleaner import cleanUp
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

INPUT_DIR = "../Crawler/Crawled_csv/ProconOrg/shortArguments/"
MODEL_DIR = "../D2V_models/"
FEATURE_VECTOR_SIZE = 20
ALPHA = 0.05


class Argument(Enum):
    PRO = 1
    CON = 2


class Topic:
    def __init__(self, name):
        self._name = name
        self._data = []  # mined arguments for this topic
        self._tagged_data = []  # tokenized data for doc2vec
        self._model = None  # doc2vec model for this topic
        self.load_data()
        self.init_model()

    def load_data(self):
        """Load arguments in csv format for this topic, clean and tokenize them"""
        data = []
        for line in open(INPUT_DIR + self._name + ".csv", 'r'):
            data.append(line.split(",")[1].rstrip())

        cleaned_data = []
        for argument in data:
            clean_argument = cleanUp(argument)
            cleaned_data.append(clean_argument)

        tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in
                       enumerate(cleaned_data)]

        self._data = cleaned_data
        self._tagged_data = tagged_data

    def init_model(self):
        """Load doc2vec model from disk, or create new model from data"""
        try:
            self._model = Doc2Vec.load(MODEL_DIR + self._name + ".model")
        except FileNotFoundError:
            # No model yet, create new model
            model = Doc2Vec(vector_size=FEATURE_VECTOR_SIZE,  # size of the feature vector
                            alpha=ALPHA,  # initial learning rate
                            min_alpha=0.00025,  # learning rate will linearly decrease to this during training
                            min_count=1  # ignores words with frequency lower than min_count
                            )

            model.build_vocab(self._tagged_data)

            model.train(self._tagged_data,
                        total_examples=model.corpus_count,
                        epochs=20
                        )

            model.save(MODEL_DIR + self._name + ".model")

    def get_counterargument(self, argument, argument_type):
        pass


if __name__ == "__main__":
    test_topic = Topic("animalTesting")
