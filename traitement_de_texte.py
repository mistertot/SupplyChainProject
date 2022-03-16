from typing import List


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
            if 'magasin' in element:
                helpvar = element.split(':')[1:]
                for i in range(6):
                    if i == 3 or i == 1:
                        helpvar[i] = float(helpvar[i])
                    else:
                        helpvar[i] = int(helpvar[i])
                magasins.append(helpvar)
                continue
           
            if 'usine' in element:
                helpvar = element.split(':')[1:]
                for i in range(6):
                    if i == 3 or i == 1:
                        helpvar[i] = float(helpvar[i])
                    else:
                        helpvar[i] = int(helpvar[i])
                usines.append(helpvar)
                continue
            
            if 'entrepot' in element:
                helpvar = element.split(':')[1:]
                for i in range(6):
                    if i == 3 or i == 1:
                        helpvar[i] = float(helpvar[i])
                    else:
                        helpvar[i] = int(helpvar[i])
                entrepots.append(helpvar)
        
        data = [usines, entrepots, magasins]
        return data

'''def recup_transport(fichier: str):

def recup_historique(fichier: str):
'''
#print(recup_param('projet info\instances\inst\A3a-params.txt'))
print(recup_sites('projet info\instances\inst\B7a-sites.txt'))