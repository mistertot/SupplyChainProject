
from magasin import Magasin 
from typing import List
class Usine :
    def __init__(self,cap_prod: int ,cout_prod: float ,cap_stock : int, cout_stock : float
    , stock_int : int, stock_fin : int ) -> None: 

        self.cap_stock : int = cap_stock #3
        self.cout_stock : float = cout_stock #4 
        self.stock_int : int = stock_int #5
        self.stock_fin : int = stock_fin #6
        self.cap_prod : float = cap_prod #1
        self.cout_prod : float = cout_prod #2
        self.Lcommande: List[Magasin] = []

    #def capacité_prod(self,magasin: Magasin):
    
    def __repr__(self) -> str:
        return "Usine : {0}; {1}; {2}; {3}; {4}; {5}".format(self.cap_prod, self.cout_prod,
         self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)

    def production(self, magasins: Magasin) -> int :
        if self.cap_prod <magasins.commande():
            return self.cap_prod
        return magasin.commande()

    def stock(self, magasin: Magasin) -> int: # definir un stock actuel (état des stock)
        
        return self.stock + self.production(magasin)

    def cap_prod_restante(self) -> int:
        return self.cap_prod - self.production()

    def demande_totale(self) -> int:
        qt: int = 0
        for k in range (len(self.Lcommande)):
            if self.Lcommande[k] != None: ### is not None:
                qt = qt + self.Lcommande[k].commande()
        return qt
    
    def capacite_restante(self) -> int:
        return self.cap_prod - self.demande_totale()
        
    
    def peut_produire(self, com: Magasin) -> bool:
        return self.capacite_restante()>=com.commande


b = [100, 1.0, 100, 0.2, 50, 50]
a = Usine(b[0], b[1], b[2], b[3], b[4], b[5])
print(a)

    










