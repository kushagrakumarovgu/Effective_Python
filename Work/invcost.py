
import csv

def inventory_cost(file_name):
    cost = 0
    with open(file_name,"r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx,row in enumerate(csv_reader):
            if idx != 0:
                cost += float(row[1]) * float(row[2])
    return cost


cost = inventory_cost("Data\inventory.csv")
print("Total cost: ",cost)
