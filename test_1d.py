# -*- coding: utf-8 -*-
"""
Utiliser ce code pour calculer une solution 1d et la tracer. L'exemple existant est celui de la chute d'un corps.

- La cellule PANNEAU DE COMMANDE DES PARAMETRES permet de déclarer les variables du problème.
- La cellule APPELS AUX FONCTIONS se charge toute seule d'appeler les fonctions souhaitées.
  Elle ne doit être modifiée que si on veut tracer plusieurs courbes, car cela implique de bidouiller les informations données à des fonctions stockées dans d'autres fichiers :)
"""
import schemas_1d, traces


#%%                     PANNEAU DE COMMANDE DES PARAMETRES

t0, T = 0, 30                                   #initialisation de l'intervalle de résolution
h = 1                                           #pas
y0 = 0                                          #solution initiale  
digits = 5                                      #précison des arrondis
f = lambda t, y : 0 - 0.00203 * y**2 + 9.81     #fonction de Cauchy (expression de f')

# Cellule à éxécuter une fois avec Ctrl+Enter avant d'appeler les fonctions ci-dessus pour que les paramètres soient pris en compte.




#%%                          APPELS AUX FONCTIONS

# Cellule à modifier seulement si on veut tracer plus d'une fonction sur un graphe.

(x, y) = schemas_1d.euler(f, y0, t0, T, h, digits=10)
traces.trace((x, y, "Méthode d'Euler"))

"""Tracé de RK4"""
(x, y) = schemas_1d.runge_kutta_4(f, y0, t0, T, h, digits=10)
traces.trace((x, y, "Méthode RK4"))
