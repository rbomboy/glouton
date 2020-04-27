# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def triRendement(L):
    """Trie une liste d'objets par rendement"""
    L.sort(key= lambda obj: obj[0]/obj[1])
    return L

def remplSac(c,L):
    """Prend en entree la capacite c (entier) et une liste d'objets tries par rendement
    retourne une liste de valeurs egales à 1 (pris) ou 0 (non pris)"""
    n=len(L)
    Lemp=[]
    for i in range(n):
        poids=L[i][0]
        if poids<=c:
            Lemp.append(1)
            c=c-poids
        else:
            Lemp.append(0)
    return Lemp
            
           
           