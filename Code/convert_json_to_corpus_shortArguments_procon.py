import os
import json
import re
import textCleaner


input_path = "../Crawler/Crawled/ProconOrg/shortArguments/"
output_path = "../Crawler/Corpus/ProconOrg/shortArguments/"

for subdir, dirs, files in os.walk(input_path):
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
        for x in data[1:]:
            if 'Pro argument' in x:
                output = open(new_output_path + str(i) + ".txt", 'w')
                # output.write("pro,")
                output.write(textCleaner.cleanUp(x['Pro argument'][0]))
                # output.write('\n')
        
            elif 'Con argument' in x:
                output = open(new_output_path  + str(i) + ".txt", 'w')
                # output.write("con,")
                output.write(textCleaner.cleanUp(x['Con argument'][0]))
                # output.write('\n')
            i += 1