import os
import json
import re
import textCleaner


input_path = "../Crawler/Crawled/ProconOrg/longArguments/"
output_path = "../Crawler/Corpus/ProconOrg/longArguments/"

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
        
        i = 0  # initiate iterator
        j = 0
        for x in data[1:]:
            if 'Pro argument' in x:
                output = open(new_output_path + "pro" + str(i) + ".txt", 'w')
                # output.write("pro,")
                output.write(textCleaner.cleanUp(x['Pro argument'][0]))
                #output.write('\n')
                #output.write(textCleaner.cleanUp(x['Pro argument text'][0:]))
                i += 1  # Iterator for filename

            elif 'Con argument' in x:
                output = open(new_output_path  + "con" + str(j) + ".txt", 'w')
                # output.write("con,")
                output.write(textCleaner.cleanUp(x['Con argument'][0]))
                #output.write('\n')
                #output.write(textCleaner.cleanUp(x['Con argument text'][0:]))
                j += 1