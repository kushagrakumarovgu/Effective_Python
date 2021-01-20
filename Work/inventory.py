

class Inventory:
    def __init__(self,products):
        self._products = products

    
    def __iter__(self):
        return iter(self._products)

    
    def __len__(self):
        return len(self._products)
    
    def __getitem__(self,index):
        return self._products[index]

    def __contains__(self,name):
        return any( p.name == name for p in self._products )

        
    
    @property
    def total_cost(self):
        return sum( p.cost for p in self._products )

    
    def tabulate_units(self):
        from collections import Counter
        t_units = Counter()
        for p in self._products:
            t_units[p.name] = t_units[p.name] + p.quant

        return t_units
