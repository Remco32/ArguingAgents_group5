import os
import json


input_file = "../Crawler/Crawled/ProconOrg/shortArguments/animalTesting.json"
output_file = "../Crawler/Crawled_csv/ProconOrg/shortArguments/animalTesting.csv"

with open(input_file) as f:
    data = json.load(f)

output = open(output_file, 'w')

for x in data[1:]:
    if 'Pro argument' in x:
        output.write("pro,")
        output.write(x['Pro argument'][0])
        output.write('\n')
    elif 'Con argument' in x:
        output.write("con,")
        output.write(x['Con argument'][0])
        output.write('\n')
