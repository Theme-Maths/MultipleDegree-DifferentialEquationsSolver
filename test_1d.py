# -*- coding: utf-8 -*-
"""
Utiliser ce code pour calculer une solution 1d et la tracer.
Conçu en cellules pour faciliter la déclaration des paramètre.
L'exemple ici présenté est celui de la chute des corps.

- La cellule PANNEAU DE COMMANDE DES PARAMETRES permet de déclarer les variables du problème.
- La cellule APPELS AUX FONCTIONS se charge d'appeler les fonctions souhaitées.
  """
  
# Cellule à éxécuter au moins une fois avec Ctrl+Enter pour importer les modules.

import schemas_1d, traces
import numpy as np
from scipy.integrate import odeint

#%%                     PANNEAU DE COMMANDE DES PARAMETRES

# Cellule à éxécuter au moins une fois avec Ctrl+Enter pour que les paramètres soient pris en compte.

t0, T = 0, 30                                   # intervalle de résolution
h = 1                                           # pas
y0 = 0                                          # solution initiale  
f = lambda t, y : 0 - 0.00203 * y**2 + 9.81     # fonction du problème de Cauchy (expression de f')


#%%                          APPELS AUX FONCTIONS

x_rk, y_rk = schemas_1d.runge_kutta_4(f, y0, t0, T, h)
x_eu, y_eu = schemas_1d.euler(f, y0, t0, T, h)
x = np.linspace(t0, T, 1000)
y = odeint(f, y0, x, tfirst = True)
traces.trace((x_eu, y_eu, "Méthode Euler"), (x_rk, y_rk, "Méthode RK4"), sol = (x, y))
