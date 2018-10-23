import os

input_path = "../Crawler/Corpus/"

def combineCorpera():
    #Check if there are two corpera for one topic (same folder name)
    for subdir, dirs, files in os.walk(input_path):
        if 'Debatabase' in dirs:

            for file in files:
                print(file)
                input_file = os.path.join(subdir, file)
            new_output_path = ""  # clear the string since we loop
            #new_output_path = output_path +
#Count the highest value in corpus 1 for both pros and cons (i.e. con9.txt -> 9)

#Loop through files in corpus 2 and increment the filename by highest value previous corpus




def combineDirectories():
#Combine directories into one single one per topic.

    return


combineCorpera()