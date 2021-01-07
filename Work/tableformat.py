
class Tableformatter:
    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError

    def row(self,row_data):
        '''
        Emit single row from table data.
        '''
        raise NotImplementedError


class TextTableFormatter(Tableformatter):
    
    def headings(self,headers):
        width = 10
        n_cols = len(headers)

        for ele in headers:
            print( '%10s' %ele,end=' ')
        else:
            print()

        dashed_line = f"{'-' * width} " * n_cols
        print(dashed_line)

    def row(self,row_data):
        
        for col in row_data:
            print(f'{col:>10s}',end=' ')
        else:
            print()

class CSVTableFormatter(Tableformatter):

    def headings(self,headers):
        print(','.join(headers))
        
    def row(self,row_data):
        print(','.join(row_data))


class HTMLTableFormatter(Tableformatter):
    def headings(self,headers):
        pass

    def row(self,row_data):
        pass