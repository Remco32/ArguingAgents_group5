from enum import Enum
from gensim.models.doc2vec import Doc2Vec

MODEL_DIR = "../D2V_models/"


class Argument(Enum):
    PRO = 1
    CON = 2


class Topic:
    def __init__(self, name):
        self._name = name
        self._data = []  # mined arguments for this topic
        self._model = None  # doc2vec model for this topic
        self.load_data()
        self.init_model()

    def load_data(self):
        pass

    def init_model(self):
        # load doc2vec model from disk, or create new model from data
        try:
            self._model = Doc2Vec.load(MODEL_DIR + self._name + ".model")
        except FileNotFoundError:
            # No model yet, create new model
            self._model = Doc2Vec()  # TODO: initialise and train new model

    def get_counterargument(self, argument, argument_type):
        pass


if __name__ == "__main__":
    test_topic = Topic("asdfdasf")
