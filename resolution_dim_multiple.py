# -*- coding: utf-8 -*-
"""
Ce fichier est chargé de résoudre les ED de dimension n, et d'interfacer les entrées utilisateur.

Contient les fonctions de résolution à plusieurs dimensions :
    - solution_dim_2(g, y0, yp0, t0, T, h, methode='rk4')
    - solution_dim_n(g, Y0, t0, T, h, methode='rk4')
    - sol_exacte_dim_2(g, y0, yp0, t0, T, h)
    - sol_exacte_dim_n(g, Y0, t0, T, h)
"""

import numpy as np
from scipy.integrate import odeint
import schemas_1d, traces
from math import cos, atan, pi, sin, exp


def solution_dim_2(g, y0, yp0, t0, T, h, methode='rk4'):
    """
    Résout une équation différentielle d'odre 2 avec la méthode choisie.
    Renvoie un tuple x, y de la solution calculé.
    
    Paramètres
    ----------
    g   : fonction du problème de Cauchy
    y0  : valeur de la solution initiale de y
    yp0 : valeur de la condition initiale de y'
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas
    methode : méthodes de résolution possibles ('euler' ou 'rk4'). Vaut 'rk4' par défaut.
    
    Renvoi
    -------
    t_list : liste des abscisses
    Y_list : liste des valeurs de calculées par la méthode
    """
    # NOTATIONS :
    # y   = y
    # yp  = y'
    # ypp = y" = g(t0, y0,  yp0) 
    
    def F(t, Y):                  # on définit la fonction F du nouveau problème de Cauchy
        (y, yp) = Y
        ypp = g(t, y, yp)         # on calcule la dernière coordonnée de ce que renverra F, à savoir ypp
        return [yp, ypp]
    
    Y0  = [y0, yp0]
    if methode == 'rk4':
        return schemas_1d.rk4_vect(F, Y0, t0, T, h)
    elif methode == 'euler':
        return schemas_1d.euler_vect(F, Y0, t0, T, h)
    else :
        raise ValueError("Méthode non reconnue. Les méthodes reconnues sont : 'rk4', 'euler'.")


def solution_dim_n(g, Y0, t0, T, h, methode='rk4'):
    """
    Résout une équation différentielle d'ordre n > 1 avec la méthode choisie.
    Renvoie un tuple (x, y) de la solution calculée.
    
    Paramètres
    ----------
    g   : fonction du problème de Cauchy (exemple dont la solution est exp(): g = lambda t, y, yp, ypp : ypp)
    Y0  : liste contenant les conditions initiales dans l'ordre suivant : Y0 = [y0, yp0, ... y_(n-1)0]
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas
    methode : méthodes de résolution possibles : 'euler', 'rk4'. Vaut 'rk4' par défaut.
    
    Renvoi
    -------
    t_list : liste des abscisses
    Y_list : liste des valeurs de calculées par la méthode
    """
    
    def F(t, Y):                  # on définit la fonction F du nouveau problème de Cauchy
        y_np1 = g(t, *Y)          # on calcule la dernière coordonnée de ce que renverra F, à savoir la valeur de la dérivées n+1ième de y en t
        return Y[1:]+[y_np1]
    
    if methode == 'rk4':
        return schemas_1d.rk4_vect(F, Y0, t0, T, h)
    elif methode == 'euler':
        return schemas_1d.euler_vect(F, Y0, t0, T, h)
    else :
        raise AttributeError("Méthode non reconnue. Les méthodes reconnues sont : 'rk4', 'euler'.")


def sol_exacte_dim_2(g, y0, yp0, t0, T, h):
    """
    Résout une équation différentielle d'ordre n avec scipy.integrate.odeint
    Renvoie un tuple x, y de la solution calculée.
    
    Paramètres
    ----------
    g   : fonction du problème de Cauchy
    y0  : valeur de la solution initiale de y
    yp0 : valeur de la condition initiale de y'
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas
    
    Renvoi
    -------
    t_list : liste des abscisses
    Y_list : liste des ordonnées de la 'solution exacte' trouvée
    """
    
    def F(t, Y):                                # on définit la fonction F du nouveau problème de Cauchy
        (y, yp) = Y
        ypp = g(t, y, yp)
        return np.array([yp, ypp])
    
    Y0 = np.array([y0, yp0])
    x = np.linspace(t0, T, int((T-t0)/h))       # on construit la liste des abscisses
    Y = odeint(F, Y0, x, tfirst=True)
    return x, Y[:,0]


def sol_exacte_dim_n(g, Y0, t0, T, h):
    """
    Résout une équation différentielle d'ordre n avec odeint, méthode la plus précise implémentée dans Python.
    Renvoie un tuple x, y de la solution calculée.
    
    Paramètres
    ----------
    g   : fonction du problème de Cauchy
    Y0  : liste contenant les conditions initiales dans l'ordre suivant : Y = [y0, yp0, ... y_(n-1)0]
    t0  : valeur de la borne inférieure de l'intervalle de résolution
    T   : valeur de la borne supérieure de l'intervalle de résolution
    h   : valeur du pas
    
    Renvoi
    -------
    t_list : liste des abscisses
    Y_list : liste des ordonnées de la 'solution exacte' trouvée
    """
    
    Y0=np.array(Y0)
    t0 = np.array(t0)
    
    def F(t, Y):                                # on définit la fonction F du nouveau problème de Cauchy
        y_np1 = g(t, *Y)
        output = Y[1:]
        return np.append(output,y_np1)
    
    x = np.linspace(t0, T, int((T-t0)/h))       # on construit la liste des abscisses
    Y = odeint(F, Y0, x, tfirst=True)
    return x, Y[:,0]


#%%                             COMMANDES DIRECTES


# EXEMPLE 1 DE LA PRESENTATION ------------------------------------------------

# # Définition de la fonction g du problème de Cauchy
# g = lambda t, y, yp : 3*yp - 20*y + 5

# # Définition des courbes que l'on veut tracer
# x1, y1 = solution_dim_2(g, 0, 0, 0, 3, 0.01, methode='rk4')
# x2, y2 = solution_dim_2(g, 0, 0, 0, 3, 0.01, methode='rk4')
# x3, y3 = solution_dim_2(g, 0, 0, 0, 3, 0.1, methode='rk4')
# xs, ys = sol_exacte_dim_2(g, 0, 0, 0, 3, 0.001)

# # Tracé des courbes
# traces.trace((x1, y1, 'Euler pas de 0.01'), (x2, y2, 'RK4 pas de 0.01'), (x3, y3, 'RK4 pas de 0.1'), sol=(xs, ys))



# EXEMPLE 2 DE LA PRESENTATION ------------------------------------------------

# # Définition de la fonction g à résoudre
# g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# # Définition des courbes que l'on veut tracer
# x1, y1 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.2, methode='euler')
# x2, y2 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.1, methode='euler')
# x3, y3 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.05, methode='euler')
# xs, ys = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 0.025)

# # Traçage des courbes
# traces.trace((x1, y1, 'Euler, pas de 0.2'),(x2, y2, 'Euler, pas de 0.1'), (x3, y3, 'Euler, pas de 0.05'), sol=(xs, ys))



# EXEMPLE DU PENDULE ----------------------------------------------------------

# # Définition de la fonction g à résoudre
# g = lambda t, y, yp : -2*0.22*yp-4**2*sin(y)

# # Définition des courbes que l'on veut tracer
# x1, y1 = solution_dim_n(g, [1.3, 0], 0, 5, 0.001, methode='euler')
# x2, y2 = solution_dim_n(g, [1.3,0], 0, 5, 0.001, methode='rk4')
# xs, ys = sol_exacte_dim_n(g, [1.3,0], 0, 5, 0.001)

# # Traçage des courbes
# traces.trace((x1, y1, 'Euler, pas de 0.001'),(x2, y2, 'RK4, pas de 0.001'), sol=(xs, ys))
