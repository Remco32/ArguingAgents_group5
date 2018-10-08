from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from textCleaner import cleanUp
import os

# data = ["Medical marijuana shows considerable promise in reducing chronic pain",
#         "As a physician, I have constantly searched for treatment options for my patients' chronic pain.",
#         "I had steadily reviewed the scientific literature on medical marijuana from the United States",
#         "The evidence is overwhelming that marijuana can relieve certain types of pain",
#         "Marijuana, or cannabis, as it is more appropriately called,\nhas been part of humanity's medicine chest for almost as long as history has\nbeen recorded"
#         ]

data = []
# input_file = "./Crawler/Crawled_csv/ProconOrg/longArguments/socialNetworking.csv"
input_folder = "./Crawler/Crawled_csv/ProconOrg/longArguments/"

for file in os.listdir(input_folder):
    for line in open(input_folder + file, 'r'):
        data.append(line.split(",")[1].rstrip())

cleaned_data = []
for argument in data:
    clean_argument = cleanUp(argument)
    cleaned_data.append(clean_argument)


# TODO: filter out stop words using nltk
tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(cleaned_data)]

epochs = 500
vec_size = 20
alpha = 0.05


def train(vec_size, alpha, epochs, tagged_data):
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

    model.save("d2v.model")


train(vec_size, alpha, epochs, tagged_data)

model = Doc2Vec.load("d2v.model")
test_data = word_tokenize("Marijuana can help relieve pain patients experience after a medical operation".lower())
test_vector = model.infer_vector(test_data)

similar = model.docvecs.most_similar([test_vector])
print(data[int(similar[0][0])])

