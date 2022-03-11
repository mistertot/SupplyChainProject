
from magasin import Magasin 

class Usine :
    def __init__(self,Capa_stocku: int ,Cout_stocku : float ,Stock_initu : int, Stock_finalu : int 
    , Capa_produ : float, Cout_produ : float ) -> None: 
    
        self.cap_stock : int = Capa_stocku
        self.cout_stock : float = Cout_stocku
        self.stock_int : int = Stock_initu
        self.stock_fin : int = Stock_finalu
        self.cap_prod : float = Capa_produ
        self.cout_prod : float = Cout_produ

    #def capacité_prod(self,magasin: Magasin):
        

    def production(self, magasin: Magasin) -> int :
        '''renvoie la charge du Camion, i.e. la quantite des commandes presentes 
        dans le camion '''
        contenue : int = 0
        for i in range (len(magasin.commande)):
            contenue = self.commande_camion[i].quantite + contenue
        return contenue

    def capacite_restante(self) -> int:
        '''renvoie la capacite restante de ce Camion (en tenant compte de
        tout ce qui a deja ete ajoute)'''
        return self.cap_prod - self.production()

    



    










