# -*- coding: utf-8 -*-
"""
Ce fichier sert à quantifier les erreurs entre une estimation et une solution de référence.
Une cellule de commandes se situe à la fin.

Contient les fonctions suivantes :
    - liste_erreur(estimation, sol)
"""

import schemas_1d, traces, resolution_dim_multiple
import numpy as np
from scipy.integrate import odeint
from math import cos, atan, exp

def liste_erreur(estimation, sol):
    """
    Renvoie une liste d'erreurs pour une estimation et un pas donnés.
    
    Paramètres
    ----------
    estimation : estimation calculée pour la résolution de l'équation différentielle
    sol     : solution exacte
    """
    (x,y) = estimation                             
    sol = list(sol)
    erreur = []
    if len(y) != len(sol[1]):
        raise ValueError ("L'estimation et la solution ne sont pas de la même longueur.")
    for i in range(len(y)):
        erreur.append(abs(y[i]-sol[1][i]))
    return erreur
    



# N.B : Dans les appels à la fonction on remarquera que dans la solution exacte, il y a des fractions avec  
# des dénominateurs (T-t0)/h+1 ou (T-t0)/h+2, cela correspond au nombre de points qu'on obtient (y compris le
# point x=t0 et x=T) lorsqu'on divise notre intervalle par le pas h.

#%%                EXEMPLE 1 DE LA PRESENTATION : Etude du pas


# Définition de la fonction g à résoudre
g = lambda t, y, yp : 3*yp - 20*y + 5

# Définition des courbes que l'on veut tracer
euler1 = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='euler')
euler2 = solution_dim_n(g, [0, 0], 0, 3, 0.005, methode='euler')
euler3 = solution_dim_n(g, [0, 0], 0, 3, 0.0025, methode='euler')
sol1 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/302)
sol2 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/602)
sol3 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/1202)
x1 = np.linspace(0, 3, 302)
x2 = np.linspace(0, 3, 602)
x3 = np.linspace(0, 3, 1202)

# Traçage des courbes
traces.trace((x1, liste_erreur(euler1, sol1), 'Erreur Euler pas de 0.01'), (x2, liste_erreur(euler2, sol2), 'Erreur Euler pas de 0.005'), (x3, liste_erreur(euler3, sol3), 'Erreur Euler pas de 0.0025'))


#%%                 EXEMPLE 2 DE LA PRESENTATION : Etude du pas

# Définition de la fonction g à résoudre
g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# Définition des courbes que l'on veut tracer
rk4_1 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.1, methode='rk4')
rk4_2 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.05, methode='rk4')
rk4_3 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.025, methode='rk4')
sol1 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/501)
sol2 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/1002)
sol3 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/2002)
x1 = np.linspace(0, 50, 501)
x2 = np.linspace(0, 50, 1002)
x3 = np.linspace(0, 50, 2002)

# Traçage des courbes
traces.trace((x1, liste_erreur(rk4_1, sol1), 'Erreur RK4 pas de 0.01'), (x2, liste_erreur(rk4_2, sol2), 'Erreur RK4 pas de 0.05'), (x3, liste_erreur(rk4_3, sol3), 'Erreur RK4 pas de 0.025'))


#%%               EXEMPLE 1 DE LA PRESENTATION : Etude des méthodes

# Définition de la fonction g à résoudre
g = lambda t, y, yp : 3*yp - 20*y + 5

# Définition des courbes que l'on veut tracer
rk4 = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='rk4')
euler = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='euler')
sol = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/302)
x = np.linspace(0, 3, 302)

# Traçage des courbes
traces.trace((x, liste_erreur(euler, sol), 'Erreur Euler pas de 0.01'), (x, liste_erreur(rk4, sol), 'Erreur RK4 pas de 0.01'))


#%%               EXEMPLE 2 DE LA PRESENTATION : Etude des méthodes

# Définition de la fonction g à résoudre
g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# Définition des courbes que l'on veut tracer
rk4 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='rk4')
euler = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='euler')
sol = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/50002)
x = np.linspace(0, 50, 50002)

# Traçage des courbes
traces.trace((x, liste_erreur(euler, sol), 'Erreur Euler pas de 0.0001'), (x, liste_erreur(rk4, sol), 'Erreur rk4 pas de 0.0001'))
