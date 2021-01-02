import csv
from pprint import pprint
from fileparse import parse_csv


def  read_inventory(file_name):

    return parse_csv(file_name,select=['name','quant','price'],types=[str,int,float])
                
def read_prices(file_name):

    return dict( parse_csv(file_name,types=[str,float],has_headers=False) )

def make_report(item_list,newprice_list):
    report = list()
    for prod in item_list:
        name = prod['name']
        quant = prod['quant']
        latest_price = newprice_list[name]
        change = prod['price'] - latest_price
        report.append( (name,quant,latest_price,change) )

    return report

def print_report(report):
    header = ('Name','Quantity','Price','Change')
    width = 10
    n_cols = len(header)
    print('%10s %10s %10s %10s' % header)
    dashed_line = f"{'-' * width} " * n_cols
    print(dashed_line)
    rupee_sym = '\u20B9'
    for name,quant,price,change in report:
        price = str(rupee_sym) + str(price)
        print(f'{name:>10s} {quant:>10d} {price:>10s} {change:>10f}')


def inventory_report(inventory_filename,prices_filename):
    products = read_inventory(inventory_filename)
    #pprint(products)
    new_prices = read_prices('Data/prices.csv')
    report = make_report(products,new_prices)
    print_report(report)

def main(argv):

    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'invfile pricefile')

    inventory_filename = argv[1]
    prices_filename = argv[2]
    inventory_report(inventory_filename,prices_filename)

if __name__ == '__main__':
    import sys
    main(sys.argv)










