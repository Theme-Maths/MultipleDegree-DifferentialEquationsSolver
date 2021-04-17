# -*- coding: utf-8 -*-
"""
Ce fichier regroupe les schémas de Euler et RK4.

Contient les fonctions de résolution en 1D :
    - euler(f, y0, t0, T, h)
    - euler_vect(F, Y0, t0, T, h)
    - runge_kutta_4(f, y0, t0, T, h)
    - rk4_vect(F, Y0, t0, T, h)
"""


def euler(f, y0, t0, T, h):
    """
    Résolution d'une ED par la méthode d'Euler explicite.
    (RAPPEL Schéma d'Euler : y_k+1 = y_k + f(y_k, t_k) * h)
     
    Paramètres
    ----------
    f  :    fonction du problème de Cauchy associé (valeur de f')
    y0 :    valeur de la condition initiale
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    
    Renvoi
    -------
    t_list : liste des valeurs de t
    y_list : liste des valeurs de y correspondantes calculées par le schéma
    """

    t_list = [t0]                  # initialisation d'une liste avec les valeurs de t
    y_list = [y0]                  # initialisation d'une liste avec les valeurs de y
    t = t0
    y = y0
    
    while t < T:                   # Tant que la date t est inférieure à la date T
        t = t + h                  # on incrémente la date avec le pas de calcul h
        t_list.append(t)
        y = y + f(t, y)*h          # on calcule la nouvelle valeur de y
        y_list.append(y)
    return t_list, y_list


def euler_vect(F, Y0, t0, T, h):
    """
    Résolution d'une ED par la méthoe d'Euler explicite sous forme vectorielle.
    (RAPPEL Schéma d'Euler : y_k+1 = y_k + f(y_k, t_k) * h)
    
    Paramètres
    ----------
    F  :    fonction du problème de Cauchy associé
    Y0 :    liste des conditions initiales [y0, yp0]
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    
    Renvoi
    -------
    t_list : liste des valeurs de t
    Y_list : liste des valeurs de y correspondantes calculées par le schéma
    """
    
    t_list = [t0]
    Y_list = [Y0]
    t = t0
    Y = Y0

    while t < T:                                         # Tant que la date t est inférieure à la date T
        t = t + h                                        # on incrémente la date avec le pas de calcul h
        t_list.append(t)
        Y = [ y + yp * h for y, yp in zip(Y, F(t, Y)) ]  # on calcule la nouvelle valeur de y
        Y_list.append(Y)
    return t_list, [Y_list[i][0] for i in range(len(Y_list))]


def runge_kutta_4(f, y0, t0, T, h) :
    """
    Résolution d'une ED par la méthoe de Runge Kutta 4.
    (RAPPEL Schéma de RK4 : y_i1 = y_i + h/6*(k1+2*k2+2*k3+k4)
    où :
    k1 = f(t_i,y_i)
    k2 = f(t_i+h/2,y_i+k1*h/2)
    k3 = f(t_i+h/2,y_i+k2*h/2)
    k4 = f(t_i+h,y_i+h*k3))
    
    Paramètres
    ----------
    f  :    fonction du problème de Cauchy associé (valeur de f')
    y0 :    valeur de la condition initiale
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    
    Renvoi
    -------
    t_list : liste des valeurs de t
    y_list : liste des valeurs de y correspondantes calculées par le schéma
    """
    
    t_list = [t0]
    y_list = [y0]
    t = t0
    y = y0

    while t < T:
        t = t + h
        t_list.append(t)
 
        k1 = f(t,y)
        k2 = f(t+h/2, y+k1*h/2)
        k3 = f(t+h/2, y+k2*h/2)
        k4 = f(t+h, y+h*k3)
        y = y + h/6*(k1+2*k2+2*k3+k4)
        y_list.append(y)
    return t_list, y_list


def rk4_vect(F, Y0, t0, T, h) :
    """
    Résolution d'une ED par la méthoe de Runge Kutta 4 sous forme vectorielle.
    (RAPPEL Schéma de RK4 : y_i1 = y_i + h/6*(k1+2*k2+2*k3+k4)
    où :
    k1 = f(t_i,y_i)
    k2 = f(t_i+h/2,y_i+k1*h/2)
    k3 = f(t_i+h/2,y_i+k2*h/2)
    k4 = f(t_i+h,y_i+h*k3))
    
    Paramètres
    ----------
    F  :    fonction du problème de Cauchy associé
    Y0 :    liste des conditions initiales [y0, yp0]
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    
    Renvoi
    -------
    t_list : liste des valeurs de t
    Y_list : liste des valeurs de y correspondantes calculées par le schéma
    """
    
    t_list = [t0]
    Y_list = [Y0]
    t = t0
    Y = Y0

    while t < T:
        t = t + h
        t_list.append(t)
        
        k1 = F(t, Y)
        k2 = F(t + h/2, [Y[i] + k1[i]*h/2 for i in range(len(Y))])
        k3 = F(t + h/2, [Y[i] + k2[i]*h/2 for i in range(len(Y))])
        k4 = F(t + h, [Y[i] + h*k3[i] for i in range(len(Y))])
        Y = [Y[i] + (h/6)*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(len(Y))]
        Y_list.append(Y)
    return t_list, [Y_list[i][0] for i in range(len(Y_list))]
