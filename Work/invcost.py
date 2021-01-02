
import csv
import sys
from report import read_inventory

def inventory_cost(file_name):
    total = 0.0
    inventory = read_inventory(file_name)
    for prod in inventory:
        total += prod['quant'] * prod['price']

    return total

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'Data\inventory.csv'

cost = inventory_cost(file_name)
print("Total cost: ",cost)


