

import product
from fileparse import parse_csv

class Inventory:
    def __init__(self):
        self._products = []

    
    def __iter__(self):
        return iter(self._products)

    
    def __len__(self):
        return len(self._products)
    
    def __getitem__(self,index):
        return self._products[index]

    def __contains__(self,name):
        return any( p.name == name for p in self._products )

    def append(self,prod):
        if isinstance(prod,product.Product):
            self._products.append(prod)
        else:
            raise TypeError(f'Expected Product object')

    @classmethod
    def from_csv(cls,lines,**opts):
        self = cls()
        invdicts = parse_csv(lines,
                            select=['name','quant','price'],
                            types=[str,int,float],
                            **opts)

        for p in invdicts: 
            self.append(product.Product(**p))
    
        return self
    
    @property
    def total_cost(self):
        return sum( p.cost for p in self._products )

    
    def tabulate_units(self):
        from collections import Counter
        t_units = Counter()
        for p in self._products:
            t_units[p.name] = t_units[p.name] + p.quant

        return t_units


