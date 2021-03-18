"""
Contient les fonctions suivantes :
    -liste_erreur : renvoie une liste contenant les erreurs calculées pour une méthode et un pas donnés
    -tableau_erreur : utilise liste_erreur afin de renvoyer un tableau contenant les erreurs pour les différents pas donnés
    -ordre_convergence : calcule l'ordre de convergence de la méthode à partir de tableau_erreur
"""

import schemas_1d
import numpy as np
from scipy.integrate import odeint

def liste_erreur(methode,sol):
    """
    Renvoie une liste d'erreurs pour une méthode et un pas donnés.
    Paramètres
    ----------
    methode : méthode utilisée pour la résolution de l'équation différentielle
    sol     : solution exacte
    digits  : précision de l'erreur
    """
    (x,y)=methode                                # liste contenant les coordonnées obtenues à l'aide de la méthode souhaitée                             
    b=list(sol)                                  #liste contenant les coordonnées obtenues avec la solution exacte
    liste=[]                                     # liste vide dans laquelle on implémentera les erreurs
    if len(y)!=len(b):
        raise ValueError ("Les deux solutions ne sont pas de la même longueur")
    for i in range(len(y)):                      # création d'une boucle pour relever les valeurs des erreurs
        liste.append(abs(y[i]-b[i][0]))
    return liste


# N.B : J'aurais pu faire autrement que travailler avec la matrice obtenue, mais j'ai remarqué qu'il y avait des erreurs d'arrondi

t0, T = 0, 1                              
n = 10   #j'ai pris le nombre de divisions de l'intervalle, c'est plus pratique                                   
y0 = 1                                      
digits = 10                                 
f = lambda t, y : y                         

methode = schemas_1d.runge_kutta_4(f, y0, t0, T, (T-t0)/10)
c = np.linspace(t0, T,10)              
d = odeint(f, y0, c, tfirst=True)
sol=d
print(liste_erreur(methode,sol))

def tableau_erreur(*erreur_pas):
    """
    Renvoie un tableau numpy (n,p) où n est le nombre de pas et p est le nombre de valeurs calculées pour ce pas
    N.B: on va prendre des pas proportionnels pour faciliter la construction du tableau
    Paramètres:
    ----------
    erreur_pas : sous la forme d'un tuple(a,b) , avec a la liste d'erreurs obtenues et b le pas, la fonction peut avoir des arguments multiples
    """