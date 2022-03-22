from sites import Site

class Magasin(Site) :
    def __build__(self) -> None: 
        super().__init__()
        #self.hist : str =  Hist_demandee 

    def __repr__(self) -> str:
        return "( Magasin : {0}; {1}; {2}; {3} )".format(self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)



    def commande (self) -> int :
        compteur : int = 0 
        for k in range(len(self.hist)):
            compteur = compteur + self.hist[k]
        return compteur/len(self.hist) 

    
        





