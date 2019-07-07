import csv

from csv_worker.dialect_customizer import CustomDialect


def row_writer(file):
    csv.register_dialect('custom1', CustomDialect)
    writer = csv.writer(file, dialect='custom1')
    writer.writerow(['1', 'ODF1', 'server3'])
    writer.writerow(['2', 'ODF1', 'server3'])
    writer.writerow(['3', 'ODF1', 'server3'])
    writer.writerow(['1', 'ODF1', 'server3'])


def dict_writer(file, quoting):
    writer = csv.DictWriter(
        file,
        fieldnames=['port', 'cross', 'server'],
        quoting=quoting,
    )
    writer.writeheader()
    writer.writerow({
        'port': 1,
        'cross': 'ODF1',
        'server': 'server2'
    })
    writer.writerow({
        'port': 2,
        'cross': 'ODF1',
        'server': 'server2'
    })
    writer.writerow({
        'port': 3,
        'cross': 'ODF1',
        'server': 'server2'
    })
    writer.writerow({
        'port': 4,
        'cross': 'ODF1',
        'server': 'server2'
    })

if __name__ == '__main__':
    new_file = 'data/undefined_dialect.csv'
    with open(new_file, 'w') as file:
        row_writer(file)
        #dict_writer(file, csv.QUOTE_NONNUMERIC)