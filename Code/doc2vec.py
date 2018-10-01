from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize


data = ["Medical marijuana shows considerable promise in reducing chronic pain",
        "As a physician, I have constantly searched for treatment options for my patients' chronic pain.",
        "I had steadily reviewed the scientific literature on medical marijuana from the United States",
        "The evidence is overwhelming that marijuana can relieve certain types of pain",
        "Marijuana, or cannabis, as it is more appropriately called,\nhas been part of humanity's medicine chest for almost as long as history has\nbeen recorded"
        ]

tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]

max_epochs = 100
vec_size = 20
alpha = 0.025

def train(vec_size, alpha, max_epochs, tagged_data):
    model = Doc2Vec(vector_size=vec_size,
                    alpha=alpha,
                    min_alpha=0.00025,
                    min_count=1,
                    dm=1)

    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
            model.train(tagged_data,
                        total_examples=model.corpus_count,
                        epochs=model.iter)

            model.alpha -= 0.0002
            model.min_alpha = model.alpha

    model.save("d2v.model")
    print("Model Saved")


train(vec_size, alpha, max_epochs, tagged_data)

model= Doc2Vec.load("d2v.model")
test_data = word_tokenize("there is evidence that marijuana is helpful in relieving certain types of pain".lower())

similar = model.docvecs.most_similar('1')
print(data[int(similar[0][0])])

