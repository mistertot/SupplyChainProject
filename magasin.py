__authors__ = 'Romain Hoaurau, Sylvain Guo, Thomas Ptr, Mustapha Rachdi'

from sites import Site

class Magasin(Site) :
    '''Une classe modelisant un site de type magasin'''    
    def __build__(self) -> None: 
        super().__init__()


    def __repr__(self) -> str:
        return "( Magasin : {0}; {1}; {2}; {3} )".format(self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)



    
        





