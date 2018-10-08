import os
import json


input_dir = "../Crawler/Crawled/ProconOrg/longArguments/"
output_dir = "../Crawler/Crawled_csv/ProconOrg/longArguments/"


if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    input_file = input_dir + file
    output_file = output_dir + file.split(".")[0] + ".csv"

    with open(input_file) as f:
        data = json.load(f)

    output = open(output_file, 'w')

    for x in data[1:]:
        if 'Pro argument' in x:
            output.write("pro,")
            output.write(x['Pro argument'][0].replace("\n", ""))
            output.write('\n')
        elif 'Con argument' in x:
            output.write("con,")
            output.write(x['Con argument'][0].replace("\n", ""))
            output.write('\n')
