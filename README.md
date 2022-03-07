# SupplyChainProject
Projet Informatique simulant une chaîne logistique.

## Programme
La classe *Probleme* définie dans le fichier *probleme.py* avec le constructeur indiqué qui
- lit les fichiers *[instance].txt* décrivant l'instance
- écrit la solution dans le fichier *[instance].sol*
- en moins de 10s

Une instance *nom* est associée à plusieurs fichiers :
- Entrées
    - *nom-params.txt* paramètres généraux
    - *nom-sites.txt* description des sites
    - *nom-transport.txt* description des transports
    - *nom-historiques.txt* historique des demandes
- Sorties
    - *nom.sol* décisions prises
- Indicateurs
    - *nom.log* messages du checker
    - *nom.kpi* états du système simulé

## Format des fichiers
