import csv

cost = 0
with open("inventory.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for idx,row in enumerate(csv_reader):
        if idx != 0:
            cost += float(row[1]) * float(row[2])

print("Price: {}".format(cost))