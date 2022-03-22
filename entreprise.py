from magasin import Magasin 
from typing import List
from usine import Usine
from entrepot import Entrepot
from transport import Transport
from traitement_de_texte import recup_sites

class Entreprise :

    def __init__(self, instance : str):
        
        sites: List = recup_sites(instance) 
        self.usines: List [Usine] = sites[0]
        self.entrepots: List[Entrepot] = sites[1]
        self.magasins: List[Magasin] = sites[2]
        

    def __repr__(self) -> str:
        return "( entreprise: {0}; {1}; {2} ".format(self.usines,self.entrepots,self.magasins) 
    
    def nb_de_commande_total(self):
        com_tot = 0
        for k in range (len(self.magasins)):
            com_tot = com_tot + self.Lcommande[k].commande 
        return com_tot


    def production(self) -> int :
        qte_prod_restante = self.nb_de_commande_total
        for p in self.usines:
            prod_non_perdu = min(p.cap_prod,p.cap_stock)
            if prod_non_perdu<qte_prod_restante:
                p.prod = prod_non_perdu 
                qte_prod_restante = qte_prod_restante - prod_non_perdu 
            else:
                p.prod = qte_prod_restante
        return qte_prod_restante

    def cout_usine(u:Usine):
        return (u.cout_stock + u.cout_prod )

    def cout_entrepot_à_usine(self):
        return 


    def tri_bulles(tab: List[float],site: List) -> List:
        sites = site.copy()
        for k in range(len(tab)):
            print(tab)
            for j in range(k-1,-1,-1):
                if tab[j]>tab[k]:
                    tab[j],tab[k] = tab[k],tab[j]
                    sites[j],sites[k]=sites[k],sites[j]
                    k=k-1
        return (tab,sites)


    def entrepot_magasin(self,m:Magasin):
        list_entrepot = []
        for e in self.entrepots:
            list_entrepot.append(e.cout_stock)
    
    def cap_restante(self,i):
        return self.entrepots[i].cap_stock
        
a = Entreprise("inst\B7a-sites.txt")
print(a)



    



