#!/usr/bin/python3
'''Projet Informatique 1A - Grenoble INP - Génie Industriel

Squelette de programme à compléter.
Rappels :
- votre programme sera appelé par un simple Probleme(instance).
- vous pouvez (devez) ajouter des méthodes, des classes, des fichiers selon vos besoins.

- Exécutez checker.py pour bénéficier du checker
- Configurer le checker via CONFIG, ne modifiez ni checker.py ni checker.exe
'''

import os.path
from entreprise import *
from numpy import savetxt

## -----------------------------------------------------------------------------
class Probleme:
    '''Classe de base du problème. Doit définir le constructeur indiqué.'''

    def __init__(self, instance: str) -> None:
        '''Résout l'instance indiquée.'''
        file: str = instance +'.sol'
        data = Entreprise(instance).sol()

        with open(file, 'w') as f:
            for champs in data:
                f.write(str(champs[0]) + ';')

                for prod in champs[1]:    
                    f.write(str(prod) )
                f.write(';')
                for trans in champs[2]:
                    f.write(str(trans) + ' ')
  
                for vente in champs[3]:
                    f.write(str(vente) + ';')
                f.write(';')
                f.write(str(champs[4]) + ';')
                f.write(str(champs[5]) + ';')
                f.write(str(champs[6]) + '\n')


## -----------------------------------------------------------------------------
if __name__ == "__main__":
    ## Choix de l'instance (lu dans CONFIG ; "mini" par défaut)
    INSTANCE = "inst\A6a"
    if os.path.exists("CONFIG"):
        with open("CONFIG", "r") as config:
            for ligne in config.readlines():
                if not '=' in ligne:
                    continue
                (var, val) = ligne.split("=")
                var = var.strip()
                val = val.strip()
                if var == "INSTANCE":
                    INSTANCE = val
                    break

    ## Résolution
    #Probleme(INSTANCE)
    p = Probleme('inst\C3a') 