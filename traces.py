# -*- coding: utf-8 -*-
"""
Ce fichier gère l'affichage des courbes sur un même graphique (de 1 à 6).

Contient les fonctions de tracés :
    - trace(x, *Y, sol=None)
"""

import matplotlib.pyplot as plt


def trace(*courbe, sol=None):
    """
    Trace un graphe représentant une à six listes et éventuellement la solution 'exacte'.

    Paramètres
    ----------
    *courbe : jusqu'à 6 tuples (x, y, name) où x et y sont des listes de valeurs et 'name' est une chaîne qui légendera la courbe x,y.
    sol     : (optionnel) tuple (x,y) de la solution 'exacte' de référence, qui sera tracée aussi. Vaut None par défaut.
    """
    
    colors = "bgrycm"                     # liste des couleurs reconnues par matplotlib
    if len(courbe) > 6:                   # Si l'utilisateur a demandé de tracer plus de 6 courbes, on lève une erreur
        raise IndexError("Impossible de tracer plus de 6 courbes.")
    
    for (x, y, name) in courbe:
        plt.plot(x, y, "{}-".format(colors[courbe.index((x, y, name))]), label=name)
        # on trace les courbes en paramétrant l'affichage avec une chaîne : une couleur parmi celles reconnues par Python ; - pour ligne continue
    
    if sol != None:                        # Si l'utilisateur a entré une solution exacte 
        plt.plot(sol[0], sol[1], "k--", label="Solution exacte")
        # on la trace avec les paramètres suivants : k pour black ; - - pour ligne pointillée

    plt.xlabel("temps")
    plt.ylabel("valeur")
    plt.legend()
    
    plt.show()
