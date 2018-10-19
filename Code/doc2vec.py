from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from textCleaner import cleanUp
import os


def train(vec_size, alpha, epochs, tagged_data, filename):
    model = Doc2Vec(vector_size=vec_size,  # size of the feature vector
                    alpha=alpha,  # initial learning rate
                    min_alpha=0.00025,  # learning rate will linearly decrease to this during training
                    min_count=1  # ignores words with frequency lower than min_count
                    )

    model.build_vocab(tagged_data)

    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=epochs
                )

    model.save("./D2V_models/" + filename.split(".")[0] + ".model")


def evaluate(model, sentence):
    model = Doc2Vec.load(model)
    test_data = word_tokenize(sentence.lower())
    test_vector = model.infer_vector(test_data)

    similar = model.docvecs.most_similar([test_vector])
    # print(data[int(similar[0][0])])
    return similar


def generate_all_models(input_folder):
    for file in os.listdir(input_folder):
        data = []
        for line in open(input_folder + file, 'r'):
            data.append(line.split(",")[1].rstrip())

        cleaned_data = []
        for argument in data:
            clean_argument = cleanUp(argument)
            cleaned_data.append(clean_argument)

        tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(cleaned_data)]

        epochs = 500
        vec_size = 20
        alpha = 0.05

        train(vec_size, alpha, epochs, tagged_data, file)


# input_folder = "./Crawler/Crawled_csv/ProconOrg/shortArguments/"
# generate_all_models(input_folder)

model_name = "./D2V_models/animalTesting.model"
print(evaluate(model_name, "animal testing"))

