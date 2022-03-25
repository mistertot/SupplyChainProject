__authors__ = 'Romain Hoaurau, Sylvain Guo, Thomas Ptr, Mustapha Rachdi'


'''fichier qui regroupe les methodes de traitement de texte
 utilisees dans la resolution du probleme'''

from typing import List
from magasin import Magasin
from usine import Usine
from entrepot import Entrepot
from re import findall

def recup_param(instance: str) -> tuple:
    '''Lit le fichier nom-params.txt et renvoie l'horizon de planification ainsi que le prix d'un produit'''
    fichier = instance + '-params.txt'
    with open(fichier,'r') as f:
        content = f.readlines()
        horizon = int(content[0])
        prix = float(content[1])
    return (horizon, prix)

def recup_sites(instance: str) -> List:
    '''Lit le fichier nom-sites.txt et initialise les différents sites''' #that's working
    fichier = instance + '-sites.txt'
    with open(fichier,'r') as f: 
        content = f.readlines()
        magasins = []
        entrepots = []
        usines = []
        for element in content:
            helpvar = element.split(':')[1:]
            for i in range(6):
                if i == 3 or i == 1:
                    helpvar[i] = float(helpvar[i])
                else:
                    helpvar[i] = int(helpvar[i])
            if 'magasin' in element:
                magasins.append(Magasin(helpvar[0], helpvar[1], helpvar[2], helpvar[3], helpvar[4], helpvar[5]))
                continue
           
            if 'usine' in element:
                usines.append(Usine(helpvar[0], helpvar[1], helpvar[2], helpvar[3], helpvar[4], helpvar[5]))
                continue
            
            if 'entrepot' in element:
                entrepots.append(Entrepot(helpvar[0], helpvar[1], helpvar[2], helpvar[3], helpvar[4], helpvar[5]))
        
        data = [usines, entrepots, magasins]
       # print(len(data[0]))
        return data

def recup_transport(instance: str)-> List:
    fichier = instance + '-transport.txt'
    with open(fichier, 'r') as f:
        L = findall('\d+', instance)
        n = int(findall('\d+', instance)[0])
        cpt = 0
        capacites = []
        couts = []
        for line in f:
            helpvar = line.split(' ')
            if cpt < n:
                for i in range(n):
                    capacites.append(int(helpvar[i]))
            else:
                for i in range(n):
                    couts.append(float(helpvar[i]))
            cpt += 1
        helplist = [(capacites[i], couts[i]) for i in range(n*n)]
        data = [helplist[i:i + n] for i in range(0, n*n, n)]
        return(data)


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
