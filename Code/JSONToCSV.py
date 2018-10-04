import json
import csv
import textCleaner

#Separate JSON elements to a CSV
def JSONToCSV(JSONFile):

    x = json.loads(JSONFile)
    f = csv.writer(open("test.csv", "w", newline=''))

    #Header for csv
    #f.writerow(["ArgumentType", "Argument"])

    for x in x:
        #if x == "Title":
        if "Title" in x:
            #print("Tit")
            print(x["Title"])
        if "Pro argument" in x:
            #print("Pro")
            print(x["Pro argument"])
        if "Con argument" in x:
            #print("Con")
            print(x["Con argument"])
        #TODO Cleanup found argument by using textCleaner
        #TODO write to CSV file

        #f.writerow([x["Title"],
#                    x["Pro argument"],
 #                   x["Con argument"]
  #                  ])



file = open("medicalMarijuana.json", "r") #open test file
content = file.read() #read content


JSONToCSV(content)