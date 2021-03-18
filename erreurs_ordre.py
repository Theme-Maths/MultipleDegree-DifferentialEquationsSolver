"""
Contient les fonctions suivantes :
    -liste_erreur : renvoie une liste contenant les erreurs calculées pour une méthode et un pas donnés
    -tableau_erreur : utilise liste_erreur afin de renvoyer un tableau contenant les erreurs pour les différents pas donnés
    -ordre_convergence : calcule l'ordre de convergence de la méthode à partir de tableau_erreur
"""

import schemas_1d
import numpy as np
from scipy.integrate import odeint

def liste_erreur(methode,sol,digits):
    """
    Renvoie une liste d'erreurs pour une méthode et un pas donnés.
    Paramètres
    ----------
    methode : méthode utilisée pour la résolution de l'équation différentielle
    sol     : solution exacte
    digits  : précision de l'erreur
    """
    (x,y)=methode                                # tuple contenant les coordonnées obtenues à l'aide de la méthode souhaitée                             
    (a,b)=sol                                    # tuple contenant les coordonnées obetenues avec la solution exacte
    l=(y-b)                                      # matrice contenant les soustractions de toutes les valeurs des tuples entre elles (je ne sais pas pourquoi ça fait ça)
    liste=[]                                     # liste vide dans laquelle on implémentera les erreurs
    for i in range(len(l)):                      # création d'une boucle pour relever les valeurs des erreurs
        liste.append(abs(l[i][i]).round(digits)) # On relève la valeur absolue des coeffs diagonaux de la liste parce qu'ils correspondent à la valeur de l'erreur
    return liste

# N.B : J'aurais pu faire autrement que travailler avec la matrice obtenue, mais j'ai remarqué qu'il y avait des erreurs d'arrondi

t0, T = 0, 1                              
n = 10    #j'ai pris le nombre de divisions de l'intervalle, c'est plus pratique                                   
y0 = 1                                      
digits = 10                                 
f = lambda t, y : y                         

methode = schemas_1d.runge_kutta_4(f, y0, t0, T, (T-t0)/n)
c = np.linspace(t0, T,n+2)              
d = odeint(f, y0, c, tfirst=True)
sol=(c,d)
print(liste_erreur(methode,sol,digits=10))

def tableau_erreur(*erreur_pas):
    """
    Renvoie un tableau numpy (n,p) où n est le nombre de pas et p est le nombre de valeurs calculées pour ce pas
    N.B: on va prendre des pas proportionnels pour faciliter la construction du tableau
    Paramètres:
    ----------
    erreur_pas : sous la forme d'un tuple(a,b) , avec a la liste d'erreurs obtenues et b le pas, la fonction peut avoir des arguments multiples
    """


