def printHeader(columnNames, tableNames, dictionary):
    print ("OUTPUT : ")
    # Table headers
    string = ""
    for col in columnNames:
        for tab in tableNames:
            if col in dictionary[tab]:
                if not string == "":
                    string += '\t'
                string += tab + '.' + col
    print (string)


def printData(fileData, columnNames, tableNames, dictionary):
    for data in fileData:
        for col in columnNames:
            print (data[dictionary[tableNames[0]].index(col)], end='\t\t')
        print('\n')
