import csv
import sys
from pprint import pprint


def  read_inventory(file_name):
    item_list = list()
    with open(file_name) as FH:
        rows = csv.reader(FH,delimiter=',')
        headers = next(rows)
        for row in rows:
            try:
                prod = { 'name' : row[0],
                         'quant' : int(row[1]),
                         'price': float(row[2]) 
                        }
                item_list.append(prod)
            except ValueError:
                print("Bad row",row)

        return item_list

            
def read_prices(file_name):
    prices = {}
    with open(file_name,"rt") as FH:
        rows = csv.reader(FH,delimiter=',')
        for row in rows:
            try:
                print(row)
                prices[row[0]] = float(row[1])
            except ValueError:
                print("Bad row",row)
            except IndexError:
                print("Bad row",row)

    return prices
                

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = "Data/inventory.csv"

items = read_inventory(file_name)

pprint(items)

prices = read_prices('Data/prices.csv')
pprint(prices)