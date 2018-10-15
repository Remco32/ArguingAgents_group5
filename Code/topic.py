from enum import Enum


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
        pass

    def get_counterargument(self, argument, argument_type):
        pass


