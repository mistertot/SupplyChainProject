

class Entrepot:
    
    def __init__(self,cap_prod: int ,cout_prod: float ,cap_stock : int, cout_stock : float
    , stock_int : int, stock_fin : int ) -> None: 

        self.cap_stock : int = cap_stock
        self.cout_stock : float = cout_stock 
        self.stock_int : int = stock_int 
        self.stock_fin : int = stock_fin
        

    def __repr__(self) -> str:
        return "Entrepot : {0}; {1}; {2}; {3}".format(self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)












