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



def solution_dim_2(g, y0, yp0, t0, T, h, methode='rk4'):
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
    methode : méthodes de résolution possibles : 'euler', 'rk4'. Vaut 'rk4' par défaut.

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
    
    if methode == 'rk4':                                             # on appelle une fonction 1D pour résoudre l'équation 1D vectorielle obtenue
        t_list, Y_list = schemas_1d.rk4_vect(F, Y0, t0, T, h)
    elif methode == 'euler':
        t_list, Y_list = schemas_1d.euler_vect(F, Y0, t0, T, h)
    else :
        raise ValueError("Méthode non reconnue. Méthodes connues : 'rk4', 'euler'.")
        
    return t_list, Y_list

def solution_dim_n(g, Y0, t0, T, h, methode='rk4'):
    """
    Résout une équation différentielle d'odre 2 avec la méthode choisie.
    Renvoie un tuple x, y de la solution calculée.
    Parameters
    ----------
    g   : fonction du problème de Cauchy (exemple dont la solution est exp(): g = lambda t, y, yp, ypp : ypp)
    Y0  : liste contenant les conditions initiales dans l'ordre suivant : Y = [y0, yp0, ... y_(n-1)0]
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas
    methode : méthodes de résolution possibles : 'euler', 'rk4'. Vaut 'rk4' par défaut.
    Returns
    -------
    t_list : liste des abscisses
    Y_list : liste des approximations trouvées pour chaque t par la fonction de résolution
    """
    
    def F(t, Y):                                                    # on définit la fonction F du nouveau problème de Cauchy
        y_np1 = g(t, *Y)                                            # on calcule la dernière coordonnée de ce que renverra F, à savoir la valeur de la dérivées n+1ième de  y_n+1
        return Y[1:]+[y_np1]                                        # on renvoie le vecteur (y', y", ..., y(dérivée n+1ième))
    
    
    if methode == 'rk4':                                             # on appelle une fonction 1D pour résoudre l'équation 1D vectorielle obtenue
        t_list, Y_list = schemas_1d.rk4_vect(F, Y0, t0, T, h)
    elif methode == 'euler':
        t_list, Y_list = schemas_1d.euler_vect(F, Y0, t0, T, h)
    else :
        raise AttributeError("Méthode non reconnue. Méthodes connues : 'rk4', 'euler'.")
        
    return t_list, Y_list

g=lambda A : ()

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
    def F(t, Y):                                                    # on définit la fonction F du nouveau problème de Cauchy
        (y, yp) = Y                                                 # on explicite les composantes de Y = (y, y')
        ypp = g(t, y, yp)                                           # on calcule la dernière coordonnée de ce que renverra F, à savoir ypp
        return np.array([yp, ypp])                                  # on renvoie le vecteur (y', y")
    
    Y0 = np.array([y0, yp0])                                        # on construit le vecteur des conditions initiales
    x = np.linspace(t0, T, int((T-t0)/h))                           # on construit la liste des abscisses
    Y = odeint(F, Y0, x, tfirst=True)                               # on appelle scipy.integrate.odeint pour résoudre le système (utilisant une version améliorée de RK4)
    return x, Y[:,1]

#%%                             COMMANDES DIRECTES

# Définition de la fonction g à résoudre
g = lambda t, y, yp : -y

# Définition des courbes que l'on veut tracer
x1, y1 = solution_dim_2(g, 1, 1, 0, 10, 0.1, methode='euler')
x2, y2 = solution_dim_2(g, 1, 1, 0, 10, 0.1, methode='rk4')
x3, y3 = solution_dim_2(g, 1, 1, 0, 10, 1, methode='rk4')
xs, ys = sol_exacte_dim_2(g, 1, 1, 0, 10, 0.01)

# Traçage des courbes
import traces
traces.trace((x1, y1, 'Euler'), (x2, y2, 'RK4'), (x3, y3, 'RK4 pas de 1'), sol=(xs, ys))


