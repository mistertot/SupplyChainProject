


from re import I


class Magasin :
    def __init__(self,Capa_stocke: int ,Cout_stocke : float ,Stock_initm : int, Stock_finalm : int
     , Hist_demandee : list[int]) -> None: 
    
        self.cap_stock : int = Capa_stocke
        self.cout_stock : float = Cout_stocke
        self.stock_int : int = Stock_initm
        self.stock_fin : int = Stock_finalm
        self.hist : str =  Hist_demandee 
        
    def commande (self) -> int :
        compteur : int = 0 
        for k in range(len(self.hist)):
            compteur = compteur + self.hist[k]
        return compteur/len(self.hist) 

    
        





