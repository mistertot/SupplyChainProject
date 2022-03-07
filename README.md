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
### *nom*-params.txt
- Ligne 1 : horizon de planification H (entier)
- Ligne 2 : prix d'un produit (nombre)
### *nom*-sites.txt
- La ligne *i* décrit le site *i*
    - champs séparés par le caractère **:**
    - ordre des champs :
        - type du site *i* (*usine* ou *entrepot* ou *magasin*)
        - capacité de produtcion *Capa_prod i* (entier)
        - coût de production *Cout_prod i* (nombre)
        - capacité de stockage *Capa_stock i* (entier)
        - coût de stockage *Cout_stock i* (nombre)
        - stock initial *Stock_init i* (entier)
        - Stock final *Stock_final i* (entier)
- L'ordre est toujours : usines puis entrepôts puis magasins
### *nom*-transport.txt
- Matrice $n\times n$ des capacités de transport (entiers)
    - la *i*-ème ligne donne les capacités des transports à partir du site *i* (l'élément ligne *i* colonne *j* est *Capa_transp i $\rightarrow$ j*)
- Puis matrice $n \times n$ des coûts de transport (nombres)
    - la *i*-ème ligne donne les capacités des transports à partir du site *i* (l'élément ligne *i* colonne *j* est *Cout_transp i $\rightarrow$ j*)
- Nombre *n* de sites et ordre connus grâce au fichier précédent
- Valeurs séparées par un ou plusieurs espaces
- Termes diagonaux et sous-diagonaux sont toujours 0 (matrice triangulaire supérieure)
### *nom*-historiques.txt
- La ligne *i* décrit la demande du *i*-ème magasin
- Valeurs (entiers) séparées par **,**
- Le nombre de valeurs est le même pour chaque ligne (chaque magasin) et est indépendant de H
### *nom*-sol
- La ligne *i* décrit les décisions du jour *i*
    - champs séparés par le caractère **;**
    - ordre des champs :
        - numéro du jour (entier)
        - production de chaque usine (entier)
        - transports (entiers)
        - ventes prévues (entier)
        - coût total de production pour ce jour (nombre)
        - coût total de stockage pour ce jour (nombre)
        - coût total de transport pour ce jour (nombre)