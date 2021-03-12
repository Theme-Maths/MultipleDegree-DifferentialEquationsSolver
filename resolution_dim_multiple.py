# -*- coding: utf-8 -*-
"""
Contient les fonctions de résolution à plusieurs dimensions :
    - solution_dim_2(g, y0, yp0, t0, T, h) :
        Résout une équation différentielle d'odre 2 avec la méthode choisie
    - sol_exacte_dim_2(g, y0, yp0, t0, T, h) :
        Résout une équation différentielle d'odre 2 avec odeint, méthode la plus précise implémentée dans Python.
"""
import numpy as np
from scipy.integrate import odeint
import schemas_1d
import math



def solution_dim_2(g, y0, yp0, t0, T, h):
    """
    Résout une équation différentielle d'odre 2 avec la méthode choisie.
    Renvoie un tuple x, y de la solution calculée.

    Parameters
    ----------
    g   : fonction du problème de Cauchy
    y0  : valeur de la solution initiale de y
    yp0 : valeur de la condition initiale de y'
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas

    Returns
    -------
    t_list : liste des abscisses
    Y_list : liste des approximations trouvées pour chaque t par la fonction de résolution

    """
    # NOTATIONS :
    # y   = y
    # yp  = y'
    # ypp = y" = g(t0, y0,  yp0) 
    
    def F(t, Y):                                                    # on définit la fonction F du nouveau problème de Cauchy
        (y, yp) = Y                                                 # on explicite les composantes de Y = (y, y')
        ypp = g(t, y, yp)                                           # on calcule la dernière coordonnée de ce que renverra F, à savoir ypp
        return [yp, ypp]                                            # on renvoie le vecteur (y', y")
    
    Y0  = [y0, yp0]                                                 # on construit le vecteur des conditions initiales
    t_list, Y_list = schemas_1d.euler_vect(F, Y0, t0, T, h)         # on appelle une fonction 1D pour résoudre l'équation 1D vectorielle obtenue
    return t_list, Y_list



def sol_exacte_dim_2(g, y0, yp0, t0, T, h):
    """
    Résout une équation différentielle d'odre 2 avec odeint, méthode la plus précise implémentée dans Python.
    Renvoie un tuple x, y de la solution calculée.

    Parameters
    ----------
    g   : fonction du problème de Cauchy
    y0  : valeur de la solution initiale de y
    yp0 : valeur de la condition initiale de y'
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas

    Returns
    -------
    t_list : liste des abscisses
    Y_list : liste des ordonnées de la 'solution exacte' trouvée

    """
    def F(Y, t):                                                    # on définit la fonction F du nouveau problème de Cauchy
        (y, yp) = Y                                                 # on explicite les composantes de Y = (y, y')
        ypp = g(t, y, yp)                                           # on calcule la dernière coordonnée de ce que renverra F, à savoir ypp
        return np.array([yp, ypp])                                  # on renvoie le vecteur (y', y")
    
    Y0 = np.array([y0, yp0])                                        # on construit le vecteur des conditions initiales
    x = np.linspace(t0, T, int((T-t0)/h))                           # on construit la liste des abscisses
    Y = odeint(F, Y0, x)                                            # on appelle scipy.integrate.odeint pour résoudre le système (utilisant une version améliorée de RK4)
    return x, Y[:,1]

#%%                             COMMANDES DIRECTES

# Définition de la fonction g à résoudre
g = lambda t, y, yp : -y

# Définition des courbes que l'on veut tracer
x1, y1 = solution_dim_2(g, 1, 0, 0, 30, 0.1)
x2, y2 = solution_dim_2(g, 1, 0, 0, 10, 0.5)
x3, y3 = solution_dim_2(g, 1, 0, 0, 5, 1)
xs, ys = sol_exacte_dim_2(g, 1, 0, 0, 30, 0.01)

# Traçage des courbes
import traces
traces.trace((x1, y1, 'pas de 0.1'), (x2, y2, 'pas de 0.5'), (x3, y3, 'pas de 1'), sol=(xs, ys))
