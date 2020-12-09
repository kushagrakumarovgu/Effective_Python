
import csv
import sys

def inventory_cost(file_name):
    total = 0.0
    with open(file_name,"rt") as FH:   # read mode for text file.
        #headers = next(FH) - NOTE: the headers will be string.
        list_of_rows = csv.reader(FH, delimiter=',')
        headers = next(list_of_rows) # skip and store the headers. Also, headers will be a list containing each column names.
        for row in list_of_rows:
            try:
                quant = int(row[1])
                price = float(row[2])
                total += quant * price
            except ValueError:           # ValueError is name of the exception due to file missing.csv
                print('Bad Error: {}'.format(row))
    return total

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'Data\inventory.csv'

cost = inventory_cost(file_name)
print("Total cost: ",cost)
