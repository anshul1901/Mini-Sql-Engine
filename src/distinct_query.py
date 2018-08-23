import csv
from collections import OrderedDict
from print_output import printHeader

def distinct(colList, columnName, tableName, dictionary):
    print ("OUTPUT :")
    string = tableName + '.' + columnName
    print (string)

    colList = list(OrderedDict.fromkeys(colList))
    for col in range(len(colList)):
        print (colList[col])


def distinctMany(columnNames, tableNames, dictionary):
    printHeader(columnNames, tableNames, dictionary)

    temp = []
    check = 0
    for tab in tableNames:
        tName = tab + '.csv'
        with open(tName, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                for col in columnNames:
                    x = row[dictionary[tableNames[0]].index(col)]
                    if x not in temp:
                        temp.append(x)
                        check = 1
                        print (x),
                if check == 1:
                    check = 0
                    print ('\n')
