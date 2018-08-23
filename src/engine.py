import csv
import sys
import re
from collections import OrderedDict
from read_data import readMetadata
from process_query import processQuery


def main():
    dictionary = {}
    readMetadata(dictionary)
    processQuery(str(sys.argv[1]), dictionary)


if __name__ == "__main__":
    main()
