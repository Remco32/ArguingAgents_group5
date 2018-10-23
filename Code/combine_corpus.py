import os
import shutil

output_path = "../Crawler/Corpus/"
corpusDirOne = "../Crawler/Corpus/Debatabase/"
corpusDirTwo = "../Crawler/Corpus/ProconOrg"

def combineCorpera():
    intersection = findIntersectionTopics()

    #Loop all directories
    for subdir, topicsCorpus, files in os.walk(corpusDirOne):
        for topic in topicsCorpus:  # directory is not empty
            if topic not in intersection: #Save to just move
                #Move directory
                shutil.move(subdir + topic, output_path)

    #For corpera of ProConOrg
    for subdir, topicsCorpus, files in os.walk(corpusDirTwo):
        if topicsCorpus and 'longArguments' not in topicsCorpus:
            for topic in topicsCorpus:  # directory is not empty
                if topic not in intersection:
                    shutil.move(subdir + '\\' + topic, output_path)
        #else:
            #combineDirectories()

    return

#Combine directories into one single one per topic.
def combineDirectories(dir1, dir2):



            #Find both directories
            #Count the highest value in corpus 1 for both pros and cons (i.e. con9.txt -> 9)
            #Loop through files in corpus 2 and increment the filename by highest value previous corpus

    return


# Check if there are two corpera for one topic (same folder name)
# Return intersection
def findIntersectionTopics():
    topicsCorpTwo = []  # for if-statement

    for subdir, dirs, files in os.walk(corpusDirOne):
        if dirs:  # directory is not empty
            topicsCorpOne = dirs

    for subdir, dirs, files in os.walk(corpusDirTwo):
        if dirs and 'longArguments' not in dirs:  # directory is not empty, and isn't root folder named longArguments (and not shortArguments)
            if not topicsCorpTwo:
                topicsCorpTwo = dirs
            else:
                topicsCorpTwo += dirs  # Add two procon corpera together
    # Find intersection of the sets, return this intersection
    return list(set(topicsCorpOne) & set(topicsCorpTwo))


combineCorpera()
