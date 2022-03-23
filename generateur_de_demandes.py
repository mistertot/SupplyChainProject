from typing import List

def recup_param(instance: str) -> tuple:
    '''Lit le fichier nom-params.txt et renvoie l'horizon de planification ainsi que le prix d'un produit'''
    fichier = instance + '-params.txt'
    with open(fichier,'r') as f:
        content = f.readlines()
        horizon = int(content[0])
        prix = float(content[1])
    return (horizon, prix)


def recup_historique(instance: str):
    
    fichier = instance +'-historiques.txt'
    historiques: list = []
    
    with open(fichier, 'r') as f:
        content = f.readlines()
        for elt in content:
            hist: list = []
            print(elt)
            helpvar = elt.split(',')
            print(helpvar)
            n = len(helpvar)
            print(n)
            for i in range(n):                   
                hist.append(int(helpvar[i]))
                print(hist)
            historiques.append(hist)

    return(historiques)



def type_demande(instance: str) -> str:
    demande = instance.split('\\')

    return demande[-1][0]

def demande_constante(instance: str, ordre_magasin: int) -> list[int]:
    n = recup_param(instance)[0]

    if type_demande(instance) == 'A':
        donnee: int = recup_historique(instance)[ordre_magasin-1][0]
        donnees : list[int] = [donnee for _ in range(n)]
        return donnees
    else:
        return [0 for _ in range(n)]




print("that's it", demande_constante('inst\A3a', 1))