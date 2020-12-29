import csv

def parse_csv(filename,select=None,types=None):
    '''
    parse a csv file and return list of record.
    '''
    records = []
    indices = []
    with open(filename) as FH:
        rows = csv.reader(FH) 
        headers = next(rows)
        if select:
            indices = [ headers.index(col) for col in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not row:   # skip rows with no data
                continue
            # Filter the row if specific columns were selected.
            if indices:
                row = [ row[index] for index in indices]

            if types:
                row = [ func(val) for func,val in zip(types,row)] 
            
            record = dict(zip(headers,row))
            records.append(record)
    return records

