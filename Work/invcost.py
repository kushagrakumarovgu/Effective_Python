
import csv
import sys

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'Data\inventory.csv'

def inventory_cost(file_name):
    total = 0.0
    with open(file_name,"rt") as FH:   # read mode for text file.
        next(FH)
        csv_reader = csv.reader(FH, delimiter=',')
        for row in csv_reader:
                quant = int(row[1])
                price = float(row[2])
                total += quant * price
    return total

cost = inventory_cost(file_name)
print("Total cost: ",cost)
