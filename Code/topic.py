from enum import Enum
from textCleaner import cleanUp
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from TFIDF import classify_argument, Argument

INPUT_DIR = "../Crawler/Crawled_csv/ProconOrg/shortArguments/"
MODEL_DIR = "../D2V_models/"
FEATURE_VECTOR_SIZE = 30
ALPHA = 0.05
EPOCHS = 40


class Topic:
    def __init__(self, name):
        self._name = name

        self._data_pro = []  # mined arguments for this topic
        self._data_con = []  # mined arguments for this topic
        self._tagged_data_pro = []  # tokenized data for doc2vec
        self._tagged_data_con = []  # tokenized data for doc2vec
        self._model_pro = None  # doc2vec model for this topic
        self._model_con = None  # doc2vec model for this topic

        self.load_data()
        self.init_model()

    def load_data(self):
        """Load arguments in csv format for this topic, clean and tokenize them"""
        data = []
        for line in open(INPUT_DIR + self._name + ".csv", 'r'):
            data.append(line.rstrip().split(","))

        cleaned_data_pro = []
        cleaned_data_con = []

        for argument in data:
            clean_argument = cleanUp(argument[1])
            if argument[0] == 'pro':
                self._data_pro.append(argument[1])
                cleaned_data_pro.append(clean_argument)
            else:
                self._data_con.append(argument[1])
                cleaned_data_con.append(clean_argument)

        tagged_data_pro = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in
                       enumerate(cleaned_data_pro)]
        tagged_data_con = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in
                       enumerate(cleaned_data_con)]

        self._tagged_data_pro = tagged_data_pro
        self._tagged_data_con = tagged_data_con

    def init_model(self):
        """Load doc2vec model from disk, or create new model from data"""
        try:
            self._model_pro = Doc2Vec.load(MODEL_DIR + self._name + "_pro.model")
            self._model_con = Doc2Vec.load(MODEL_DIR + self._name + "_con.model")
        except FileNotFoundError:
            # No model yet, create new model
            self._model_pro = Doc2Vec(vector_size=FEATURE_VECTOR_SIZE,  # size of the feature vector
                            alpha=ALPHA,  # initial learning rate
                            min_alpha=0.00025,  # learning rate will linearly decrease to this during training
                            min_count=1  # ignores words with frequency lower than min_count
                            )
            self._model_con = Doc2Vec(vector_size=FEATURE_VECTOR_SIZE,  # size of the feature vector
                            alpha=ALPHA,  # initial learning rate
                            min_alpha=0.00025,  # learning rate will linearly decrease to this during training
                            min_count=1  # ignores words with frequency lower than min_count
                            )

            self._model_pro.build_vocab(self._tagged_data_pro)
            self._model_con.build_vocab(self._tagged_data_con)

            self._model_pro.train(self._tagged_data_pro,
                        total_examples=self._model_pro.corpus_count,
                        epochs=EPOCHS
                        )
            self._model_con.train(self._tagged_data_con,
                        total_examples=self._model_con.corpus_count,
                        epochs=EPOCHS
                        )

            self._model_pro.save(MODEL_DIR + self._name + "_pro.model")
            self._model_con.save(MODEL_DIR + self._name + "_con.model")

    def get_counterargument(self, argument, argument_type):
        test_data = word_tokenize(argument.lower())
        if argument_type == Argument.CON:
            test_vector = self._model_pro.infer_vector(test_data)
            similar = self._model_pro.docvecs.most_similar([test_vector])
            ca = self._data_pro[int(similar[0][0])]
            print(self._model_con.docvecs.most_similar([test_vector]))
        else:
            test_vector = self._model_con.infer_vector(test_data)
            similar = self._model_con.docvecs.most_similar([test_vector])
            ca = self._data_con[int(similar[0][0])]
            print(self._model_con.docvecs.most_similar([test_vector]))

        return ca


if __name__ == "__main__":
    test_topic = Topic("socialNetworking")
    argument = "Being part of social media will decrease the quality of life of people and increase the risk of health problems"
    # argument_type = classify_argument(argument, test_topic._name)
    argument_type = Argument.CON
    counter_argument = test_topic.get_counterargument(argument, argument_type)
    print(counter_argument)