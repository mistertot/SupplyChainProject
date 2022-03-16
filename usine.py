
from magasin import Magasin 
from typing import List
class Usine :
    def __init__(self,Capa_stocku: int ,Cout_stocku : float ,Stock_initu : int, Stock_finalu : int 
    , Capa_produ : float, Cout_produ : float ) -> None: 
    
        self.cap_stock : int = Capa_stocku 
        self.cout_stock : float = Cout_stocku 
        self.stock_int : int = Stock_initu 
        self.stock_fin : int = Stock_finalu
        self.cap_prod : float = Capa_produ
        self.cout_prod : float = Cout_produ
        self.Lcommande: List[Magasin] = []

    #def capacité_prod(self,magasin: Magasin):
    

    def production(self, magasins: Magasin) -> int :
        if self.cap_prod <magasin.commande():
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




    










