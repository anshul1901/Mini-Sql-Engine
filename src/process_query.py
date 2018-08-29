import re
import sys
from distinct_query import distinctMany
from select_columns import selectColumns
from where_query import *
from join_query import join
from aggregate_query import aggregate


def processQuery(query, dictionary):
    query = (re.sub(' +', ' ', query)).strip()

    if "from" in query:
        obj1 = query.split('from')
    else:
        sys.exit("Incorrect Syntax")

    obj1[0] = (re.sub(' +', ' ', obj1[0])).strip()

    if "select" not in obj1[0].lower():
        sys.exit("Incorrect Syntax")
    # print object
    object1 = obj1[0][7:]

    object1 = (re.sub(' +', ' ', object1)).strip()

    l = []
    l.append("select")

    if "distinct" in object1 and "distinct(" not in object1:
        object1 = object1[9:]
        l.append("distinct")

    l.append(object1)
    object1 = l

    # select distinct List<colnames> from <table>
    object3 = ""
    if "distinct" in object1[1] and "distinct(" not in object1[1]:
        object3 = object1[1]
        object3 = (re.sub(' +', ' ', object3)).strip()
        object1[1] = object1[2]

    colStr = object1[1]
    colStr = (re.sub(' +', ' ', colStr)).strip()
    columnNames = colStr.split(',')
    for i in columnNames:
        columnNames[columnNames.index(i)] = (re.sub(' +', ' ', i)).strip()

    obj1[1] = (re.sub(' +', ' ', obj1[1])).strip()
    object2 = obj1[1].split('where')

    tableStr = object2[0]
    tableStr = (re.sub(' +', ' ', tableStr)).strip()
    tableNames = tableStr.split(',')
    for i in tableNames:
        tableNames[tableNames.index(i)] = (re.sub(' +', ' ', i)).strip()
    for i in tableNames:
        if i not in dictionary.keys():
            error = "[ERROR]: Table '" + i + "' doesn't exist"
            sys.exit(error)

    if len(object2) > 1 and len(tableNames) == 1:
        object2[1] = (re.sub(' +', ' ', object2[1])).strip()
        processWhere(object2[1], columnNames, tableNames, dictionary)
        return
    elif len(object2) > 1 and len(tableNames) > 1:
        object2[1] = (re.sub(' +', ' ', object2[1])).strip()
        processWhereJoin(object2[1], columnNames, tableNames, dictionary)
        return

    if(len(tableNames) > 1):
        join(columnNames, tableNames, dictionary)
        return

    if object3 == "distinct":
        distinctMany(columnNames, tableNames, dictionary)
        return

    if len(columnNames) == 1:
        # aggregate -- Assuming (len(columnNames) == 1) i.e aggregate function
        for col in columnNames:
            if '(' in col and ')' in col:
                funcName = ""
                colName = ""
                a1 = col.split('(')
                funcName = (re.sub(' +', ' ', a1[0])).strip()
                colName = (re.sub(' +', ' ', a1[1].split(')')[0])).strip()
                aggregate(funcName, colName, tableNames[0], dictionary)
                return
            elif '(' in col or ')' in col:
                sys.exit("Syntax error")

    selectColumns(columnNames, tableNames, dictionary)
