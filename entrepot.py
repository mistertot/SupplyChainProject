from sites import Site


class Entrepot(Site):
    def __build__(self) -> None: 
        super().__init__()
        

    def __repr__(self) -> str:
        return "( Entrepot : {0}; {1}; {2}; {3} )".format(self.cap_stock, self.cout_stock, self.stock_int, self.stock_fin)












