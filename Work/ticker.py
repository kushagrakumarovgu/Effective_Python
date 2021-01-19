import csv
from follow import follow


def parse_product_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('Data/marketlog.csv')
    rows = parse_product_data(lines)
    
    for row in rows:
        print(row)