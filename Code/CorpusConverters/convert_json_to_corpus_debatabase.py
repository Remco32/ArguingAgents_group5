import os
import json
import re
from Code import textCleaner

input_path = "../Crawler/Crawled/Debatabase/"
output_path = "../Crawler/Corpus/Debatabase/"

#filthy hack
def numberingFix(iterator):
    #filthy hack
    numbering = iterator
    if numbering < 10:
        numbering = '0' + str(numbering)
    return str(numbering)



for subdir, dirs, files in os.walk(input_path):
    print (subdir)
    print (dirs)
    #Go though all the files in the path
    for file in files:
        input_file = os.path.join(subdir, file)
        new_output_path = "" #clear the string since we loop
        new_output_path = output_path + re.sub('.json$', "", file) + "/" #remove extentsion, add forward slash for directory
        if not os.path.exists(new_output_path):
            os.makedirs(new_output_path)

        with open(input_file) as f:
            data = json.load(f)
        
        i = 0  # initiate iterator pros
        j = 0  # iterator cons
        for x in data[1:]:
            if 'Pro argument' in x:

                output = open(new_output_path + "pro" + numberingFix(i) + ".txt", 'w', encoding="utf-8")
                proArg = textCleaner.removeJunk(x['Pro argument'][0:])
                output.write(proArg)
                output.write('\n')
                output.write(textCleaner.removeJunk(x['Point'][0:]))
                i += 1  # Iterator for filename

                #Counter point to pro argument
                output = open(new_output_path + "con" + numberingFix(j) + ".txt", 'w', encoding="utf-8")
                output.write(proArg)
                output.write('\n')
                output.write(textCleaner.removeJunk(x['Counterpoint'][0:]))
                j += 1



            elif 'Con argument' in x:
                output = open(new_output_path  + "con" + numberingFix(j) + ".txt", 'w', encoding="utf-8")
                conArg = textCleaner.removeJunk(x['Con argument'][0:])
                output.write(conArg)
                output.write('\n')
                output.write(textCleaner.removeJunk(x['Point'][0:]))
                j += 1

                #Counter point con argument
                output = open(new_output_path  + "pro" + numberingFix(i) + ".txt", 'w', encoding="utf-8")
                output.write(conArg)
                output.write('\n')
                output.write(textCleaner.removeJunk(x['Counterpoint'][0:]))
                i += 1

