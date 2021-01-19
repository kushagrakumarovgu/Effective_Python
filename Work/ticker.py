import csv
from follow import follow
from report import read_inventory

def filter_names(rows,names):
    for row in rows:
        if row['name'] in names:
            yield row

def convert_types(rows,types):
    for row in rows:
        yield [ func(val) for func, val in zip(types,row) ]

def make_dicts(rows,headers):
    for row in rows:
        yield dict(zip(headers,row))

def select_columns(rows,indices):
    for row in rows:
        yield [ row[idx] for idx in indices]

def parse_product_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    rows = convert_types(rows,[str,float,float])
    rows = make_dicts(rows,['name','price','change'])
    return rows

if __name__ == '__main__':
    inventory = read_inventory('Data/inventory.csv')

    lines = follow('Data/marketlog.csv')
    rows = parse_product_data(lines)

    rows = filter_names(rows,inventory)
    
    for row in rows:
        print(row)