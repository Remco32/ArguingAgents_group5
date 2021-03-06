import os
from os import listdir
import shutil
import re

output_path = "../Crawler/Corpus/"
corpusDirOne = "../Crawler/Corpus/Debatabase/"
corpusDirTwo = "../Crawler/Corpus/ProconOrg"

def combineCorpera(intersectionBool):
    intersection = []
    if intersectionBool is True:
        intersection = findIntersectionTopics()

    #Loop all directories
    for subdir, topicsCorpus, files in os.walk(corpusDirOne):
        for topic in topicsCorpus:  # directory is not empty
            if topic not in intersection: #Save to just move
                #Move directory
                if not os.path.exists(output_path  + topic):
                    os.makedirs(output_path  + topic)
                copytree(subdir + topic, output_path + topic)

    #For corpera of ProConOrg
    for subdir, topicsCorpus, files in os.walk(corpusDirTwo):
        if topicsCorpus and 'longArguments' not in topicsCorpus:
            for topic in topicsCorpus:  # directory is not empty
                if topic not in intersection:
                    if not os.path.exists(output_path  + topic):
                        os.makedirs(output_path + '/' + topic)

                    copytree(subdir + '/' + topic, output_path + '/' + topic)


#For the corpera with intersection between them
def combineRemainingCorpera():
    #Move remaining corpera, which have intersection
    for subdir1, topicsCorpus1, files1 in os.walk(corpusDirOne):
        for subdir2, topicsCorpus2, files2 in os.walk(corpusDirTwo):
            if topicsCorpus2 and 'longArguments' not in topicsCorpus2:
                for topic1 in topicsCorpus1:
                    for topic2 in topicsCorpus2:
                        if topic1 == topic2:
                            combineDirectories(subdir1, subdir2, topic1)
    combineCorpera(False) #once more for the intersection

#Combine directories into one single one per topic.
def combineDirectories(dir1, dir2, topic):
        #Count the amount of pros and cons in a corpus
        amountOfProArguments = len(listdir(dir1+topic))/2 #Dir1 is a directory of the debatabase. The debatabase has the same number of pro as con arguments

        #Loop through files in corpus 2 and
        for subdir, topicsCorpus, files in os.walk(dir2 + '\\' + topic):
            #Get number of the argument
            for file in reversed(files): #reversed so bigger filenumbers don't get overwritten first

                firstChar = file[0]
                number = (file[3:])
                number = int(re.sub('\.txt$', '', number))
                #increment number by amountOfProArguments
                number += int(amountOfProArguments)
                number = str(number)

                #change the filename
                if firstChar == 'c':
                    os.rename(dir2 + '\\' + topic + '\\' + file, dir2 + '\\' + topic + '\\' + 'con' + number + '.txt')
                if firstChar == 'p':
                    os.rename(dir2 + '\\' + topic + '\\' + file, dir2 + '\\' + topic + '\\' + 'pro' + number + '.txt')



        #Move files from corpus one



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


#Workaround for restriction of shutil: requires to copy to non-existing folder otherwiste.
#Adapted from https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = src + '/' + item
        d = dst + '/' + item
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy(s, d)

def removeOldDirs(): #TLeaves files behind, only on my end. Works on Linux.
    shutil.rmtree(corpusDirOne, ignore_errors=True) #Ignore remaining files
    shutil.rmtree(corpusDirTwo, ignore_errors=True)




#Run
combineCorpera(True)
combineRemainingCorpera()
removeOldDirs()