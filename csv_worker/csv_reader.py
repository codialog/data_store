import csv

with open('data/same_data.csv', 'r') as f:
    """read as array"""
    #reader = csv.reader(f)
    """read as dictionary"""
    reader = csv.DictReader(f)
    print('Line num: {}'.format(reader.line_num))
    print('Dialect: {}'.format(reader.dialect))
    for row in reader:
        print(row)