from magasin import Magasin 
from typing import List
from usine import Usine
from entrepot import Entrepot
from transport import Transport
from traitement_de_texte import recup_sites

class Entreprise :

    def __init__(self, path : str):
        self.usines: List [Usine] = recup_sites(path)[0]
        self.entrepots: List[Entrepot] = recup_sites(path)[1]
        self.magasins: List[Magasin] = recup_sites(path)[2]
        

    def __repr__(self) -> str:
        return "( entreprise: {0}; {1}; {2} ".format(self.usines,self.entrepots,self.magasins) 
    
    def nb_de_commande_total(self):
        com_tot = 0
        for k in range (len(self.magasins)):
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
        return (u.cout_stock + u.cout_prod )

    #def entrepot_magasin(self,m:Magasin):
     #   for e in self.Lentrepot:

a = Entreprise("inst\B7a-sites.txt")
print(a)



    



