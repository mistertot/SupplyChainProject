
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
    

    def production(self, magasin: Magasin) -> int :
        '''renvoie la charge du Camion, i.e. la quantite des commandes presentes 
        dans le camion '''
        if self.cap_prod<magasin.commande():
            return self.cap_prod
        return magasin.commande()

    def cap_prod_restante(self) -> int:
        '''renvoie la capacite restante de ce Camion (en tenant compte de
        tout ce qui a deja ete ajoute)'''
        return self.cap_prod - self.production()

    def demande_totale(self) -> int:
        '''renvoie la charge du Camion, i.e. la quantite des commandes presentes 
        dans le camion '''
        qt: int = 0
        for k in range (len(self.Lcommande)):
            if self.Lcommande[k] != None: ### is not None:
                qt = qt + self.Lcommande[k].commande()
        return qt
    
    def capacite_restante(self) -> int:
        '''renvoie la capacite restante de ce Camion (en tenant compte de
        tout ce qui a deja ete ajoute)'''
        return self.cap_prod - self.demande_totale()
        
    
    def peut_contenir(self, com: Magasin) -> bool:
        ''' renvoie vrai si et seulement si la commande c peut etre ajoutee à
        ce Camion sans de#TODOer la capacite (en tenant compte de tout
        ce qui a deja été ajoute)'''
        return self.capacite_restante()>=com.commande



    










