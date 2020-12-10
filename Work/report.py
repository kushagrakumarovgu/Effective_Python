import csv
import sys


def  read_inventory(file_name):
    item_list = list()
    with open(file_name) as FH:
        rows = csv.reader(FH,delimiter=',')
        headers = next(rows)
        for row in rows:
            try:
                name = row[0]
                quant = int(row[1])
                price = float(row[2])
                item_list.append((name,quant,price))
            except ValueError:
                print("Bad row",row)

        return item_list

            


try:
    file_name = sys.argv[1]
except IndexError:
    file_name = "Data/inventory.csv"

items = read_inventory(file_name)

print(items)