import csv
import sys
from pprint import pprint


def  read_inventory(file_name):
    item_list = list()
    with open(file_name) as FH:
        rows = csv.reader(FH,delimiter=',')
        headers = next(rows)
        for line_no,row in enumerate(rows,start=1):
            try:
                prod = { 'name' : row[0],
                         'quant' : int(row[1]),
                         'price': float(row[2]) 
                        }
                item_list.append(prod)
            except ValueError:
                print("{} Bad row: {}".format(line_no,row))

        return item_list

            
def read_prices(file_name):
    prices = {}
    with open(file_name,"rt") as FH:
        rows = csv.reader(FH,delimiter=',')
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except (ValueError,IndexError):
                print("Bad row",row)

    return prices

def make_report(item_list,newprice_list):
    report = list()
    for prod in item_list:
        name = prod['name']
        quant = prod['quant']
        latest_price = newprice_list[name]
        change = prod['price'] - latest_price
        report.append( (name,quant,latest_price,change) )

    return report

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = "Data/inventory.csv"

products = read_inventory(file_name)
pprint(products)

newprice_list = read_prices('Data/prices.csv')
pprint(newprice_list)
price = 0.0
latest_price = 0.0
for prod in products:
    price += prod['quant'] * prod['price'] 
    latest_price += prod['quant'] * newprice_list[prod['name']]

print("Total Gain: {}".format((price - latest_price)))

report = make_report(products,newprice_list)

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








