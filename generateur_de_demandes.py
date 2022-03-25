__authors__ = 'Romain Hoaurau, Sylvain Guo, Thomas Ptr, Mustapha Rachdi'


'''fichier qui regroupe les methodes utiles dans la generation des demandes'''
def recup_param(instance: str) -> tuple:
    '''Lit le fichier nom-params.txt et renvoie l'horizon de planification ainsi que le prix d'un produit'''
    fichier = instance + '-params.txt'
    with open(fichier,'r') as f:
        content = f.readlines()
        horizon = int(content[0])
        prix = float(content[1])
    return (horizon, prix)


def recup_historique(instance: str):
    '''recupere le fichier nom-historique.tx et renvoie l'historique des magasins sous forme 
    d'une liste'''
    fichier = instance +'-historiques.txt'
    historiques: list = []
    
    with open(fichier, 'r') as f:
        content = f.readlines()
        for elt in content:
            hist: list = []

            helpvar = elt.split(',')

            n = len(helpvar)

            for i in range(n):                   
                hist.append(int(helpvar[i]))

            historiques.append(hist)

    return(historiques)



