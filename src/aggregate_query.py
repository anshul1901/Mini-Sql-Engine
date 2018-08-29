import sys
from read_data import readFile
from distinct_query import distinct


def aggregate(func, columnName, tableName, dictionary):

    # print('[FROM AGGREGATE]', dictionary)
    if columnName == '*':
        sys.exit("[ERROR]: sql query syntax error, aggregate functions not applicable on *")
    if columnName not in dictionary[tableName]:
        error = "[ERROR]: no column named " + columnName + " found in " + tableName
        sys.exit(error)

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
        print ("[ERROR]: unknown function :", '"' + func + '"')
