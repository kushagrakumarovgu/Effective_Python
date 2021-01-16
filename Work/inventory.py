

class Inventory:
    def __init__(self,products):
        self._products = products

    
    def __iter__(self):
        return iter(self._products)
        
    
    @property
    def total_cost(self):
        return sum([ p.cost for p in self._products])

    
    def tabulate_units(self):
        from collections import Counter
        t_units = Counter()
        for p in self._products:
            t_units[p.name] = t_units[p.name] + p.quant

        return t_units
