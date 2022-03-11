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

## -----------------------------------------------------------------------------
class Probleme:
    '''Classe de base du problème. Doit définir le constructeur indiqué.'''

    def __init__(self, instance: str) -> None:
        '''Résout l'instance indiquée.'''
        pass #TODO

## -----------------------------------------------------------------------------
if __name__ == "__main__":
    ## Choix de l'instance (lu dans CONFIG ; "mini" par défaut)
    INSTANCE = "mini"
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
    Probleme(INSTANCE)