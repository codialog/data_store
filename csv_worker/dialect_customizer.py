import csv


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = '*'
    delimiter = '!'
    lineterminator = '\n'
