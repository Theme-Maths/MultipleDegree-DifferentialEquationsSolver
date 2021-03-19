# -*- coding: utf-8 -*-
"""
Contient les fonctions de tracés :
    - trace(x, *Y, sol=None):
        Trace un graphe représentant une à six listes et éventuellement la solution réelle.
"""

import matplotlib.pyplot as plt


def trace(*courbe, sol=None):
    """
    Trace un graphe représentant une à six listes et éventuellement la solution réelle.

    Paramètres
    ----------
    *courbe : jusqu'à 6 tuples (x, y, name) où x et y sont des listes de valeurs et 'name' est une chaîne qui légendera la courbe x,y.
    sol     : (optionnel) couple (x,y) de la solution réelle, qui sera tracée aussi. Vaut None par défaut.
    """
    
    colors = "bgrycm"                                               #initiales des couleurs reconnues par Python
    if len(courbe) > 6:                                             #si l'utilisateur a demandé de tracer plus de 6 courbes, on lève une erreur
        raise IndexError("Impossible de tracer plus de 6 courbes.")
    
    for (x, y, name) in courbe:                                     #Pour toutes les courbes demandées
        plt.plot(x, y, "{}-+".format(colors[courbe.index((x, y, name))]), label=name)
        #on entre la courbe correspondante en paramétrant l'affichage : une couleur parmi celles reconnues par Python ; - pour ligne continue ; + pour les marqueurs en forme de plus
    
    if sol != None:                                                 #Si l'utilisateur a entré une solution exacte 
        plt.plot(sol[0], sol[1], "k--", label="solution exacte")
        #on l'entre avec les paramètres suivants : k pour black ; - - pour ligne pointillée

    plt.xlabel("temps")                                             #nom de l'axe des abscisses
    plt.ylabel("y")                                                 #nom de l'axe des ordonnées
    plt.legend()                                                    #localisation de la légende dans le coin en bas à droite
 
    plt.show()                                                      #on montre le graphique
