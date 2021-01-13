'''
Defines product class.
'''
class Product:
    '''
    Class for a product consisting of name , quant and price. 
    '''
    def __init__(self,name,quant,price):
        self.name = name
        self.quant = quant
        self.price = price

    @property
    def cost(self):
        '''
        Return the cost of the product.
        '''
        return self.quant * self.price

    def sell(self,sold_quant):
        '''
        Sell few units of the product.
        '''
        self.quant -= sold_quant

    def __repr__(self):
        #return f'Product("{self.name}",{self.quant},{self.price:0.2f})'
        # !r gives the internal representation of the variable in f string.
        return f'Product({self.name!r},{self.quant!r},{self.price!r})'