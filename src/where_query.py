from read_data import readFile
from print_output import printHeader


def processWhere(whereStr, columnNames, tableNames, dictionary):
    a = whereStr.split(" ")

    # print (a)

    if(len(columnNames) == 1 and columnNames[0] == '*'):
        columnNames = dictionary[tableNames[0]]

    printHeader(columnNames, tableNames, dictionary)

    tName = tableNames[0] + '.csv'
    fileData = []
    readFile(tName, fileData)

    check = 0
    for data in fileData:
        string = evaluate(a, tableNames, dictionary, data)
        for col in columnNames:
            if eval(string):
                check = 1
                print (data[dictionary[tableNames[0]].index(col)], end="\t\t")
        if check == 1:
            check = 0
            print ('\n')


def processWhereJoin(whereStr, columnNames, tableNames, dictionary):
    tableNames.reverse()

    l1 = []
    l2 = []
    readFile(tableNames[0] + '.csv', l1)
    readFile(tableNames[1] + '.csv', l2)

    fileData = []
    for item1 in l1:
        for item2 in l2:
            fileData.append(item2 + item1)

    dictionary["sample"] = []
    for i in dictionary[tableNames[1]]:
        dictionary["sample"].append(tableNames[1] + '.' + i)
    for i in dictionary[tableNames[0]]:
        dictionary["sample"].append(tableNames[0] + '.' + i)

    dictionary["test"] = dictionary[tableNames[1]] + dictionary[tableNames[0]]

    tableNames.remove(tableNames[0])
    tableNames.remove(tableNames[0])
    tableNames.insert(0, "sample")

    if(len(columnNames) == 1 and columnNames[0] == '*'):
        columnNames = dictionary[tableNames[0]]

    for i in columnNames:
        print (i, end='\t')
    print ('\n')

    a = whereStr.split(" ")

    check = 0
    for data in fileData:
        string = evaluate(a, tableNames, dictionary, data)
        for col in columnNames:
            if eval(string):
                check = 1
                if '.' in col:
                    print (data[dictionary[tableNames[0]].index(col)], end='\t\t')
                else:
                    print (data[dictionary["test"].index(col)], end='\t\t')
        if check == 1:
            check = 0
            print ('\n')

    del dictionary['sample']


def evaluate(a, tableNames, dictionary, data):
    string = ""
    for i in a:
        # print (i)
        if i == '=':
            string += i*2
        elif i in dictionary[tableNames[0]]:
            string += data[dictionary[tableNames[0]].index(i)]
        elif i.lower() == 'and' or i.lower() == 'or':
            string += ' ' + i.lower() + ' '
        else:
            string += i
        # print (string)
    return string
