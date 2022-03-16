


from re import I


class Magasin :
    def __init__(self,cap_prod: int ,cout_prod: float ,cap_stock : int, cout_stock : float
    , stock_int : int, stock_fin : int ) -> None: 

        self.cap_stock : int = cap_stock
        self.cout_stock : float = cout_stock 
        self.stock_int : int = stock_int 
        self.stock_fin : int = stock_fin
        self.cap_prod : float = cap_prod
        self.cout_prod : float = cout_prod
    
    def __repr__(self) -> str:
        return "Magasin : {0}; {1}; {2}; {3}; {4}; {5}".format(self.cap_prod, self.cout_prod,
         self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)

    
    def commande (self) -> int :
        compteur : int = 0
        for k in range(len(self.hist)):
            compteur =+ compteur + self.hist[k]
        return compteur

    
        





