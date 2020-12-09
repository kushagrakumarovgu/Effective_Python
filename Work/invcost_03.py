
import csv

def inventory_cost(file_name):
    total = 0.0
    with open(file_name,"r") as FH:
        next(FH)
        csv_reader = csv.reader(FH, delimiter=',')
        for row in csv_reader:
                quant = int(row[1])
                price = float(row[2])
                total += quant * price
    return total


cost = inventory_cost("Data\inventory.csv")
print("Total cost: ",cost)
