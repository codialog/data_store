import csv


def print_file(file):
    reader = csv.reader(file)
    for row in reader:
        print(row)


def sniff_dialect(file):
    sniffer = csv.Sniffer()
    file.seek(0)
    content = file.read()
    dialect = sniffer.sniff(content)
    print(dialect.delimiter, dialect.doublequote, dialect.quoting)
    return dialect


def print_with_dialect(file, dialect):
    file.seek(0)
    reader = csv.reader(file, dialect=dialect)
    for row in reader:
        print(row)


if __name__ == '__main__':
    read_file = 'data/undefined_dialect.csv'
    with open(read_file, 'r') as file:
        print_file(file)
        dialect = sniff_dialect(file)
        print_with_dialect(file, dialect)