from typing import List
from magasin import Magasin
from usine import Usine
from entrepot import Entrepot

def recup_param(fichier: str) -> tuple:
    with open(fichier,'r') as f:
        content = f.readlines()
        horizon = int(content[0])
        prix = float(content[1])
    return (horizon, prix)

def recup_sites(fichier: str) -> List:
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
        return data

'''def recup_transport(fichier: str):

def recup_historique(fichier: str):
'''
#print(recup_param('projet info\instances\inst\A3a-params.txt'))
print(recup_sites('inst\A3a-sites.txt'))