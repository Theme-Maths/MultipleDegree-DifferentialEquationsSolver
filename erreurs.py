# -*- coding: utf-8 -*-
"""
Contient les fonctions suivantes :
    -liste_erreur : renvoie une liste contenant les erreurs calculées pour une méthode et un pas donnés
    -tableau_erreur : utilise liste_erreur afin de renvoyer un tableau contenant les erreurs pour les différents pas donnés
    -ordre_convergence : calcule l'ordre de convergence de la méthode à partir de tableau_erreur
"""

import schemas_1d, traces
from schemas_1d import euler, runge_kutta_4
import numpy as np
from scipy.integrate import odeint
from math import cos, atan, exp
from resolution_dim_multiple import solution_dim_n, sol_exacte_dim_n

def liste_erreur(estimation,sol):
    """
    Renvoie une liste d'erreurs pour une estimation et un pas donnés.
    Paramètres
    ----------
    estimation : estimation calculée pour la résolution de l'équation différentielle (par une certaine méthode)
    sol     : solution exacte
    """
    (x, y)=estimation                             # liste contenant les coordonnées obtenues à l'aide de la méthode souhaitée                             
    b=list(sol)                                   #liste contenant les coordonnées obtenues avec la solution exacte
    liste=[]                                      # liste vide dans laquelle on implémentera les erreurs
    if len(y)!=len(b[1]):                         # on ajoute cette condition pour s'assurer que le nombre de points calculés
                                                  # avec la méthode est exactement le même qu'avec odeint, et donc pour éviter 
                                                  # de relever des valeurs d'erreurs erronées
        raise ValueError ("L'estimation et la solution ne sont pas de la même longueur.") 
    for i in range(len(y)):                      # création d'une boucle pour relever les valeurs des erreurs
        liste.append(abs(y[i]-b[1][i]))
    return liste

   
#%%                           COMMANDES DIRECTES

"""
N.B : Dans les appels à la fonction on remarquera que dans la solution exacte, il y a des fractions avec  
des dénominateurs (T-t0)/h+1 ou (T-t0)/h+2, cela correspond au nombre de points qu'on obtient (y compris le
point x=t0 et x=T) qu'on obtient lorsqu'on divise notre intervalle par le pas h

"""
# Définition de la fonction g à résoudre
#g = lambda t, y, yp : 3*yp - 20*y + 5

# # Définition des courbes que l'on veut tracer
#euler1 = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='euler')
#euler2 = solution_dim_n(g, [0, 0], 0, 3, 0.005, methode='euler')
#euler3 = solution_dim_n(g, [0, 0], 0, 3, 0.0025, methode='euler')
#sol1 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/302)
#sol2 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/602)
#sol3 = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/1202)
#c = np.linspace(0, 3, 302)
#d = np.linspace(0, 3, 602)
#e =np.linspace(0, 3, 1202)
# # Traçage des courbes
#traces.trace((c, liste_erreur(euler1, sol1), 'Erreur Euler pas de 0.01'),(d, liste_erreur(euler2, sol2), 'Erreur Euler pas de 0.005'),(e, liste_erreur(euler3, sol3), 'Erreur Euler pas de 0.0025'))

# # Définition de la fonction g à résoudre
#g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# # Définition des courbes que l'on veut tracer
#rk4_1 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.1, methode='rk4')
#rk4_2 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.05, methode='rk4')
#rk4_3 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.025, methode='rk4')
#sol1 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/501)
#sol2 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/1002)
#sol3 = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/2002)
#c = np.linspace(0, 50, 501)
#d = np.linspace(0, 50, 1002)
#e = np.linspace(0, 50, 2002)
# # Traçage des courbes
#traces.trace((c, liste_erreur(rk4_1, sol1), 'Erreur RK4 pas de 0.01'),(d, liste_erreur(rk4_2, sol2), 'Erreur RK4 pas de 0.05'),(e, liste_erreur(rk4_3, sol3), 'Erreur RK4 pas de 0.025'))

# # Définition de la fonction g à résoudre
#g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# # Définition des courbes que l'on veut tracer
#rk4 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='rk4')
#euler = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='euler')
#sol = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/50002)
#c = np.linspace(0, 50, 50002)
# # Traçage des courbes
#traces.trace((c, liste_erreur(euler, sol), 'Erreur Euler pas de 0.0001'),(c, liste_erreur(rk4, sol), 'Erreur rk4 pas de 0.0001'))

# # Définition de la fonction g à résoudre
#g = lambda t, y, yp : 3*yp - 20*y + 5

# # Définition des courbes que l'on veut tracer
#rk4 = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='rk4')
#euler = solution_dim_n(g, [0, 0], 0, 3, 0.01, methode='euler')
#sol = sol_exacte_dim_n(g, [0, 0], 0, 3, 3/302)
#c = np.linspace(0, 3, 302)
# # Traçage des courbes
#traces.trace((c, liste_erreur(euler, sol), 'Erreur Euler pas de 0.01'),(c, liste_erreur(rk4, sol), 'Erreur RK4 pas de 0.01'))

# # Définition de la fonction g à résoudre
#g = lambda t, y, yp, ypp: 1/4 * (cos(t*ypp) - atan(yp))

# # Définition des courbes que l'on veut tracer
#rk4 = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='rk4')
#euler = solution_dim_n(g, [0, 0, 0], 0, 50, 0.001, methode='euler')
#sol = sol_exacte_dim_n(g, [0, 0, 0], 0, 50, 50/50002)
#c = np.linspace(0, 50, 50002)
# # Traçage des courbes
#traces.trace((c, liste_erreur(euler, sol), 'Erreur Euler pas de 0.0001'),(c, liste_erreur(rk4, sol), 'Erreur rk4 pas de 0.0001'))
