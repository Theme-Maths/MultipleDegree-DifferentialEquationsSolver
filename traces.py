# -*- coding: utf-8 -*-
"""
Contient les fonctions de tracés :
    - trace(x, *Y, sol=None):
        Trace un graphe représentant une à six listes et éventuellement la solution réelle.
"""

import matplotlib.pyplot as plt


def trace(x, *Y, sol=None):
    """
    Trace un graphe avec x comme abscisses, une à six listes y en ordonnées et éventuellement la solution réelle.

    Paramètres
    ----------
    x : liste de valeurs à tracer en abcisses
    *Y : liste(s) de valeurs à tracer en ordonnées, peut contenir 6 listes au maximum
    sol : (optionnel) couple (x,y) de la solution réelle, qui sera tracée aussi. Vaut None par défaut.
    """
    
    colors = "bgrycm"                                 #initiales des couleurs reconnues par Python
    if len(Y) > 6:                                    #si l'utilisateur a demandé de tracer plus de 6 courbes, on lève une erreur
        raise IndexError("Impossible de tracer plus de 6 courbes.")
    
    for y in Y:                                       #Pour toutes les courbes demandées
        plt.plot(x, y, "{}-+".format(colors[Y.index(y)]), label="estimation n°{}".format(Y.index(y) + 1))
        #on entre la courbe correspondante en paramétrant l'affichage : une couleur parmi celles reconnues par Python ; - pour ligne continue ; + pour les marqueurs en forme de plus
    
    if sol != None:                                   #si l'utilisateur a entré une solution exacte 
        plt.plot(sol[0], sol[1], "k--+", label="solution exacte")
        #on l'entre avec les paramètres suivants : k pour black ; - - pour ligne pointillée, + pour les marqueurs en forme de plus


    plt.xlabel("temps")                               #nom de l'axe des abscisses
    plt.ylabel("y")                                   #nom de l'axe des ordonnées
    plt.legend(loc='lower right')                     #localisation de la légende dans le coin en bas à droite
    
    plt.show()                                        #on montre le graphique