import csv
from follow import follow

def select_columns(rows,indices):
    for row in rows:
        yield [ row[idx] for idx in indices]

def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    return rows

if __name__ == '__main__':
    lines = follow('Data/marketlog.csv')
    rows = parse_product_data(lines)
    
    for row in rows:
        print(row)