import csv
from report import read_inventory


def inventory_cost(file_name):
    total = 0.0
    inventory = read_inventory(file_name)
    for prod in inventory:
        total += prod.cost

    return total

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'invfile')

    filename = argv[1]    
    cost = inventory_cost(filename)
    print("Total cost: ",cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

