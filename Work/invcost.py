
import csv
import sys

def inventory_cost(file_name):
    total = 0.0
    with open(file_name,"rt") as FH:   # read mode for text file.
        #headers = next(FH)  NOTE: the headers will be string.
        list_of_rows = csv.reader(FH, delimiter=',')
        headers = next(list_of_rows) # skip and store the headers. Also, headers will be a list containing each column names.
        for line_no,row in enumerate(list_of_rows,start=1):
            try:
                row_dict = dict(zip(headers,row))
                quant = int(row_dict['quant'])
                price = float(row_dict['price'])
                total += quant * price
            except ValueError:           # ValueError is name of the exception due to file missing.csv
                print('{} Bad Row: {}'.format(line_no,row))
    return total

try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'Data\inventory.csv'
     

cost = inventory_cost(file_name)
print("Total cost: ",cost)
