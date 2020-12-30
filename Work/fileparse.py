import csv

def parse_csv(filename,select=None,types=None,has_headers=True,delimiter=','):
    '''
    parse a csv file and return list of record.
    '''
    indices = []
    if select and not has_headers:
        raise RuntimeError(f'select argument requires columns headers') 

    with open(filename) as FH:
        rows = csv.reader(FH,delimiter=delimiter)

        if has_headers: 
            headers = next(rows)
        
            if select:
                indices = [ headers.index(col) for col in select]
                headers = select     
        
        records = []
        for row in rows:
            if not row:   # skip rows with no data
                continue
            # Filter the row if specific columns were selected.
            if indices:
                row = [ row[index] for index in indices]

            if types:
                row = [ func(val) for func,val in zip(types,row)] 
            
            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)
            
            records.append(record)

    return records

