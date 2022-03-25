__authors__ = 'Romain Hoaurau, Sylvain Guo, Thomas Ptr, Mustapha Rachdi'

from magasin import Magasin 
from typing import List
from sites import Site

class Usine(Site):
    '''Une classe modelisant un site de type usine'''
    def __build__(self) -> None: 
        super().__init__()

    
    def __repr__(self) -> str:
        return "( Usine : {0}; {1}; {2}; {3}; {4}; {5} )".format(self.cap_prod, self.cout_prod,
         self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)


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


    










