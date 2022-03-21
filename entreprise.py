from magasin import Magasin 
from typing import List
from usine import Usine
from entrepot import Entrepot


class Entreprise :

    def __init__(self,nbMagasin,nbUsine,nbEntrepot):
        self.Lcommande: List[Magasin] = []
        self.Lusine: List [Usine] = []
        
    def nb_de_commande_total(self):
        com_tot = 0
        for k in range (len(self.Lcommande)):
            com_tot = com_tot + self.Lcommande[k].commande 
        return com_tot


    def production(self) -> int :
        qte_prod_restante = self.nb_de_commande_total
        for p in self.Lusine:
            prod_non_perdu = min(p.cap_prod,p.cap_stock)
            if prod_non_perdu<qte_prod_restante:
                p.prod = prod_non_perdu 
                qte_prod_restante = qte_prod_restante - prod_non_perdu 
            else:
                p.prod = qte_prod_restante
        return qte_prod_restante

    def cout_usine(u:Usine):
        return (u.cout_stock + u.cout_prod)

    def cout_total(self) -> float:
        for m in self.Lcommande:

    



