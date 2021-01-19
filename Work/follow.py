import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0,os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        
        yield line

if __name__ == "__main__":
    import report
    inventory = report.read_inventory('Data/inventory.csv')
    for line in follow('Data/marketlog.csv'):

        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in inventory:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


