import sys
from read_data import readFile
from print_output import *


def selectColumns(columnNames, tableNames, dictionary):

    if len(columnNames) == 1 and columnNames[0] == '*':
        columnNames = dictionary[tableNames[0]]

    for i in columnNames:
        if i not in dictionary[tableNames[0]]:
            error = "[ERROR]: no column named '" + \
                i + "' found in " + tableNames[0]
            sys.exit(error)

    printHeader(columnNames, tableNames, dictionary)

    tName = tableNames[0] + '.csv'
    fileData = []
    readFile(tName, fileData)

    printData(fileData, columnNames, tableNames, dictionary)
