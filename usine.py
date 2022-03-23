
from magasin import Magasin 
from typing import List
from sites import Site

class Usine(Site):
    def __build__(self) -> None: 
        super().__init__()
        #self.Lcommande: List[Magasin] = []

    #def capacité_prod(self,magasin: Magasin):
    
    def __repr__(self) -> str:
        return "( Usine : {0}; {1}; {2}; {3}; {4}; {5} )".format(self.cap_prod, self.cout_prod,
         self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)

    def peut_produire(self, quantite: int) -> bool:
        return  self.cap_prod <=  quantite
    
    def production(self, quantite: int) -> bool :
        if self.peut_produire(quantite):
            return self.cap_prod
        return magasins.commande()

    


    # def stock(self, magasin: Magasin) -> int: # definir un stock actuel (état des stock)
        
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
#print(a)

    










