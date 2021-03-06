import csv
from pprint import pprint
from fileparse import parse_csv
from product import Product
from tableformat import create_formatter
from inventory import Inventory



def  read_inventory(file_name,**opts):

    with open(file_name) as FH:       
        return Inventory.from_csv(FH,**opts)
                
def read_prices(file_name):
    with open(file_name) as FH:
        return dict( parse_csv(FH,types=[str,float],has_headers=False) )

def make_report(item_list,newprice_list):
    report = list()
    for prod in item_list:
        name = prod.name
        quant = prod.quant
        latest_price = newprice_list[name]
        change = prod.price - latest_price
        report.append( (name,quant,latest_price,change) )

    return report

def print_report(report,formatter):
    header = ('Name','Quantity','Price','Change')
    formatter.headings(header)
    rupee_sym = '\u20B9'
    for name,quant,price,change in report:
        price = str(rupee_sym) + f'{price:0.2f}'
        row_data = [name, str(quant), price,f'{change:>0.2f}']
        formatter.row(row_data)


def inventory_report(inventory_filename,prices_filename,fmt='txt'):
    products = read_inventory(inventory_filename)
    new_prices = read_prices('Data/prices.csv')
    report = make_report(products,new_prices)
    formatter = create_formatter(fmt)
    print_report(report,formatter)

def main(argv):

    if len(argv) != 4:
        raise SystemExit(f'Usage: {argv[0]} ' 'invfile pricefile format')

    inventory_filename = argv[1]
    prices_filename = argv[2]
    fmt = argv[3]

    inventory_report(inventory_filename,prices_filename,fmt)

import logging
logging.basicConfig(filename = 'report.log',
                    level = logging.DEBUG,
                    filemode = 'a')

if __name__ == '__main__':
    import sys
    main(sys.argv)










