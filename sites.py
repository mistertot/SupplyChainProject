


class Site:
    '''Classe representant un site, qui pourrait etre une usine, en entrepot ou un magasin'''
    def __init__(self,cap_prod: int ,cout_prod: float ,cap_stock : int, cout_stock : float
    , stock_int : int, stock_fin : int ) -> None: 

        self.cap_prod : float = cap_prod #1
        self.cout_prod : float = cout_prod #2        
        self.cap_stock : int = cap_stock #3
        self.cout_stock : float = cout_stock #4 
        self.stock_int : int = stock_int #5
        self.stock_fin : int = stock_fin #6
    
    def stock_actuel(self):
        pass
