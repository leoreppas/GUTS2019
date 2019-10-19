import csv

def process(file):
    text = []
    labels = []
    with open(file) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            text.append(row[0])
            labels.append(row[1])

    return(text,labels)