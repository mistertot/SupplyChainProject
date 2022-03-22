from magasin import Magasin 
from typing import List
from sites import Site
from usine import Usine
from entrepot import Entrepot
from transport import Transport
from traitement_de_texte import recup_sites

class Entreprise :

    def __init__(self, instance : str):
        
        self.instance : str = instance
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

    def cout_magasin(self, ordre_usine: int, ordre_magasin: int):
        '''l'ordre c'est l'ordre reel et non pas la position dans la liste'''
        #le 1er c'est 1 et non pas 0 (bisous)
        cout_transport: float = Transport(self.instance, ordre_usine, ordre_magasin + len(self.usines) + len(self.entrepots)).data[1]

        print(cout_transport)
        sans_entrepot: float = self.usines[ordre_usine-1].cout_prod + self.magasins[ordre_magasin-1].cout_stock + self.usines[ordre_usine-1].cout_stock + cout_transport
        
        #print("1: {0}, 2: {1}, 3: {2}, 4: {3}".format(self.usines[ordre_usine-1].cout_prod, self.magasins[ordre_magasin-1].cout_stock , self.usines[ordre_usine-1].cout_stock, cout_transport))
        
        return sans_entrepot


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


    '''def tri_bulles(tab: List[float],site: List) -> List:
        sites = site.copy()
        for k in range(len(tab)):
            print(tab)
            for j in range(k-1,-1,-1):
                if tab[j]>tab[k]:
                    tab[j],tab[k] = tab[k],tab[j]
                    sites[j],sites[k]=sites[k],sites[j]
                    k=k-1
        return (tab,sites)'''


    def entrepot_magasin(self,m:Magasin):
        list_entrepot = []
        for e in self.entrepots:
            list_entrepot.append(e.cout_stock)
    
    def cap_restante(self,i):
        return self.entrepots[i].cap_stock
        
a = Entreprise("inst\B7a")
#print(a)
#print(len(a.usines), len(a.magasins), len(a.entrepots))
#b =Transport(a.instance, 1, 1 + len(a.usines) + len(a.entrepots)).data[1]
#print(b)        
print(a.cout_magasin(1,1))



    



