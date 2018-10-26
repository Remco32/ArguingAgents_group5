import os

from TFIDF import classify_argument, classify_argument_2
from topic import Topic
from textCleaner import cleanUp


if __name__ == "__main__":
    topics = []

    for folder in os.listdir("../Crawler/Corpus/"):
        topics.append(folder)

    while True:
        i = 1
        for topic in topics:
            print(str(i) + ") " + topic)
            i += 1

        choice = topics[int(input("Choose a topic: ")) - 1]
        topic_object = Topic(choice)

        while True:
            function = input(
                 choice + ":\n1) List arguments \n2) Classify argument and get counterargument \n3) Go back to topics \n")
            if function == "1":
                topic_object.list_arguments()
            if function == "2":
                argument = cleanUp(input("Give argument: \n"))

                argument_type = classify_argument_2(argument)
                print("Argument was classified as: " + argument_type.value)

                ca = topic_object.get_counterargument(argument, argument_type)
                print("Counterargument:" + ca)
            if function == "3":
                break
