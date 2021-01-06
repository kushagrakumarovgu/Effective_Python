
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