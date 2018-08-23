import csv

def readMetadata(dictionary):
    f = open('./metadata.txt', 'r')
    check = 0
    for line in f:
        if line.strip() == "<begin_table>":
            check = 1
            continue
        if check == 1:
            tableName = line.strip()
            dictionary[tableName] = []
            check = 0
            continue
        if not line.strip() == '<end_table>':
            dictionary[tableName].append(line.strip())

def readFile(tName,fileData):
        with open(tName,'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for row in reader:
                fileData.append(row)