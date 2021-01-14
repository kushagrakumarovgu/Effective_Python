import csv

def parse_csv(lines,select=None,types=None,has_headers=True,delimiter=',',silence_errors=False):
    '''
    parse a csv file and return list of record.
    '''
    indices = []
    if select and not has_headers:
        raise RuntimeError(f'select argument requires columns headers') 

    if isinstance(lines, str):
        raise RuntimeError(f'lines argument should be an iterable object like a file object or a list')

    rows = csv.reader(lines,delimiter=delimiter)

    if has_headers: 
        headers = next(rows)
        
        if select:
            indices = [ headers.index(col) for col in select]
            headers = select     
        
    records = []
    for line_no,row in enumerate(rows,start=1):
        if not row:   # skip rows with no data
            continue
        # Filter the row if specific columns were selected.
        if indices:
            row = [ row[index] for index in indices]

        if types:
            try:
                row = [ func(val) for func,val in zip(types,row)] 
            except ValueError as e:
                if not silence_errors:
                    print("Row{}: Couldn't convert {}".format(line_no,row))
                    print("Row{}: {}".format(line_no,e))
                continue
            
        if has_headers:
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        
        records.append(record)

    return records

