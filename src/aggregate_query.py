import sys
from read_data import readFile
from distinct_query import distinct


def aggregate(func, columnName, tableName, dictionary):

    if columnName == '*':
        sys.exit("error")
    if columnName not in dictionary[tableName]:
        sys.exit("error")

    tName = tableName + '.csv'
    fileData = []
    readFile(tName, fileData)
    colList = []
    for data in fileData:
        colList.append(int(data[dictionary[tableName].index(columnName)]))

    if func.lower() == 'max':
        print (max(colList))
    elif func.lower() == 'min':
        print (min(colList))
    elif func.lower() == 'sum':
        print (sum(colList))
    elif func.lower() == 'avg':
        print (sum(colList)/len(colList))
    elif func.lower() == 'distinct':
        distinct(colList, columnName, tableName, dictionary)
    else:
        print ("ERROR")
        print ("Unknown function : ", '"' + func + '"')
