from generateur_de_demandes import recup_param , recup_historique
from magasin import Magasin 
from typing import List
from sites import Site
from usine import Usine
from entrepot import Entrepot
from transport import Transport
from traitement_de_texte import recup_sites, recup_transport
import traitement_de_texte
import time





class Entreprise :

    def __init__(self, instance : str):
        
        self.instance : str = instance
        sites: List = traitement_de_texte.recup_sites(instance) 
        self.usines: List [Usine] = sites[0]
        self.entrepots: List[Entrepot] = sites[1]
        self.magasins: List[Magasin] = sites[2]
        self.historique = recup_historique(instance)
        self.horizon: int = recup_param(instance)[0]
        self.prix: float = recup_param(instance)[1]
        self.transportt = traitement_de_texte.recup_transport(instance)

    
    def commande (self,m) -> int :
        compteur : int = 0 
        for k in range(len(self.historique[m])):
            compteur = compteur + self.historique[m][k]
        return int(compteur/len(self.historique[m]))+1 

    def __repr__(self) -> str:
        return "( entreprise: {0}; {1}; {2} ".format(self.usines,self.entrepots,self.magasins) 

    
    def nb_de_commande_total(self):
        com_tot = 0
        for k in range (len(self.magasins)):
            com_tot = com_tot + self.commande(k)
        return com_tot

    def liste_com(self):
        lst_com = []
        for k in range(len(self.magasins)):
            lst_com.append(self.commande(k))
        return lst_com

    def cout_magasin(self, ordre_usine: int, ordre_magasin: int):
        '''l'ordre c'est l'ordre reel et non pas la position dans la liste'''
        #le 1er c'est 1 et non pas 0 (bisous)
        cout_transport: float = Transport(self.instance, ordre_usine, ordre_magasin + len(self.usines) + len(self.entrepots)).data[1]

        # print(cout_transport)
        sans_entrepot: float = self.usines[ordre_usine-1].cout_prod + self.magasins[ordre_magasin-1].cout_stock + self.usines[ordre_usine-1].cout_stock + cout_transport
        
        #print("1: {0}, 2: {1}, 3: {2}, 4: {3}".format(self.usines[ordre_usine-1].cout_prod, self.magasins[ordre_magasin-1].cout_stock , self.usines[ordre_usine-1].cout_stock, cout_transport))
        
        return sans_entrepot


    def production(self) -> List[int] :
        usi = []
        qte_prod_restante = self.nb_de_commande_total()
        for k in range (len(self.usines)):
            prod_non_perdu = min(int(self.usines[k].cap_prod),int(self.usines[k].cap_stock))
            if prod_non_perdu<qte_prod_restante: #verifie si l'usine peut produire à la qte demandé
                usi.append(prod_non_perdu) #si non on produit le maximum posible
                qte_prod_restante = qte_prod_restante - prod_non_perdu 
            else: #si oui on produit la quantité necessaire
                usi.append(qte_prod_restante)
                qte_prod_restante = 0  
        return usi #renvoie la liste des qte produite pour chaque usine



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

    def trans(self):
        nbu = len(self.usines)
        nbe = len(self.entrepots)
        nbm = len(self.magasins)
        nbs = nbu+nbe+nbm
        tr = []
        for i in range(nbs):
            tr.append([])
            for j in range (nbs):
                tr[i].append(0) #cree un tableau rempli de zero au depart
        p = self.production().copy()
        #puis on insert la quantite transferer du site i(ligne) au site j(colonne) selon notre strategie
        for u in range (nbu):
            for m in range (nbu+nbe,nbs):
                if self.commande(m-nbu-nbe)<p[u]:
                    tr[u][m]=self.commande(m-nbu-nbe)
                    p[u] = p[u] - self.commande(m-nbu-nbe)
                else:
                    tr[u][m]=p[u]
                    p[u] = 0
        return tr

    def cout_prod_tot(self):
        cprod = 0
        for p in range(len(self.production())):
            cprod = cprod + self.production()[p]*self.usines[p].cout_prod
        return cprod

    def arrive_stock(self,i:int): #renvoie ce qui arrive dans le stock
        a = 0
        for k in range (len(self.trans())): #ca correspond a la colonne du site i
            a = a + self.trans()[k][i]
        return a

    def depart_stock(self,i:int): #renvoie ce qui est envoyer depuit le stock 
        d = 0
        for k in range (len(self.trans())):#ca correspond a la ligne du site i
            d = d + self.trans()[i][k]
        return d 


    def stock_sites(self): #renvoie un tableau ou chaque sous liste donne l'etat du stock de chaque site jour apres jour
        l = [[]]
        nbu = len(self.usines)
        nbe = len(self.entrepots)
        nbm = len(self.magasins)
        nbs = nbu+nbe+nbm
        for u in range (nbu):
            l[0].append(self.usines[u].stock_int)
        for e in range (nbe):
            l[0].append(self.entrepots[e].stock_int)
        for m in range (nbm):
            l[0].append(self.magasins[m].stock_int)
        for j in range(1,self.horizon):
            cop = l[j-1].copy()
            for k in range(nbs):
                cop[k]= cop[k] + self.arrive_stock(k) - self.depart_stock(k) #le stock c'est le stock du jour d'avant + ce qui arrive - ce qui est envoyer
            for us in range(nbu):
                cop[us] = cop[us] + self.production()[us] #on ajoute le production au stock de l'usine
            for ma in range (nbu+nbe,nbs):
                cop[ma] = cop[ma]- self.commande(ma-(nbu+nbe)) #on retire ce la vente prevue du jour j au stock de magasin
            l.append(cop)
        return(l)

    def cout_total_stock(self,j:int): #renvoie le cout total du stock du jour j
        cst =0
        for k in range (len(self.stock_sites()[0])):
            cst = cst + self.stock_sites()[j][k]
        return cst


    def cout_trans(self): #renvoie le cout de transpoert total
        ctrans = 0
        for i in range(len(self.trans())):
            for j in range(len(self.trans())):
                ctrans = ctrans + self.trans()[i][j]*self.transportt[i][j][1]
        return(ctrans)



    def sol(self): #renvoie un tableau ou chaque ligne i est la une liste represantant le jour i du fichier sol
        L = [] 
        for j in range(self.horizon): 
            L.append([]) 
            L[-1].append(j+1) #renvoie le jour
            L[-1].append(self.production()) #renvoie une liste de la production de chaque usine
            ltr = []
            for k in self.trans():
                ltr = ltr + k
            L[-1].append(ltr) #renvoie la matrice transport aplatie
            L[-1].append(self.liste_com()) #renvoie une liste montrant la commande prevue pour chaque magasin
            L[-1].append(self.cout_prod_tot()) #renvoie le cout total de production du jour 
            L[-1].append(self.cout_total_stock(j)) #renvoie le cout total du stock du jour 
            L[-1].append(self.cout_trans()) #renvoie le cout total de transport du jour
        return L 

    
    


a = Entreprise("inst\B3b")
print(a.sol())
end = time.time()
print ("prod:")
print(a.production())
print ('time:' )
print(end - start)
#print(a)
#print(len(a.usines), len(a.magasins), len(a.entrepots))
#b =Transport(a.instance, 1, 1 + len(a.usines) + len(a.entrepots)).data[1]
#print(b)        
#print(a.cout_magasin(1,1))





    



