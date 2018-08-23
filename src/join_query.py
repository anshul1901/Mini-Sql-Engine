from read_data import readFile

def join(columnNames, tableNames, dictionary):
    tableNames.reverse()

    l1 = []
    l2 = []
    readFile(tableNames[0] + '.csv', l1)
    readFile(tableNames[1] + '.csv', l2)

    fileData = []
    for item1 in l1:
        for item2 in l2:
            fileData.append(item2 + item1)

    # dictionary["sample"] = dictionary[b] + dictionary[a]
    dictionary["sample"] = []
    for i in dictionary[tableNames[1]]:
        dictionary["sample"].append(tableNames[1] + '.' + i)
    for i in dictionary[tableNames[0]]:
        dictionary["sample"].append(tableNames[0] + '.' + i)

    dictionary["test"] = dictionary[tableNames[1]] + dictionary[tableNames[0]]
    # print (dictionary["test"])

    tableNames.remove(tableNames[0])
    tableNames.remove(tableNames[0])
    tableNames.insert(0, "sample")

    if(len(columnNames) == 1 and columnNames[0] == '*'):
        columnNames = dictionary[tableNames[0]]

    # print (header)
    for i in columnNames:
        print (i, end='\t')
    print

    # printData(fileData,columnNames,tableNames,dictionary)

    for data in fileData:
        for col in columnNames:
            if '.' in col:
                print (data[dictionary[tableNames[0]].index(col)], end='\t\t')
            else:
                print (data[dictionary["test"].index(col)], end='\t\t')
        print ('\n')

    # del dictionary[tableNames[0]]
