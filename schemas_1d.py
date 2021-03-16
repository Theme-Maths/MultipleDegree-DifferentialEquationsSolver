# -*- coding: utf-8 -*-
"""
Contient les fonctions de résolution en 1D :
    - euler(f, y0, t0, T, h, digits=10) :
            Résolution par la métgode d'Euler explicite.
            Renvoie un tuple (x, y) contenant les listes x et y
    - euler_vect(F, Y0, t0, T, h) :
            Idem que précéedemment, mais où les Y sont des vecteurs
    - runge_kutta_4(f, y0, t0, T, h, digits=10) :
            Résolution par le méthode de Runge Kutta d'ordre 4.
            Renvoie un tuple (x, y) contenant les listes x et y
"""



def euler(f, y0, t0, T, h, digits=10):
    """
    Résolution d'une EDO 1D par la méthoe d'Euler explicite.
    (RAPPEL Schéma d'Euler : y_k+1 = y_k + f(y_k, t_k) * h)

    Paramètres
    ----------
    f  :    fonction du problème de Cauchy associé (valeur de f')
    y0 :    valeur de la condition initiale
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    digits :(optionel) nombre de décimales des arrondis, 10 par défaut

    Renvoi
    -------
    t_list : liste des valeurs de t
    y_list : liste des valeurs de y correspondantes calculées par le schéma

    """

    t_list = [t0]                        #initialisation d'une liste avec les valeurs de t
    y_list = [y0]                        #initialisation d'une liste avec les valeurs de y
    t = t0                               #initialisation de t à t0, la borne inf de l'intervalle de résolution
    y = y0                               #initialisation de y à y0, la condition initiale

    while t < T:                         #Tant que la date t est inférieure à la date T
       t = t + h                         #on incrémente la date avec le pas de calcul h
       t_list.append(round(t,digits))    #on ajoute cette nouvelle date à la fin de la liste des dates (round = arrondi à "digits" décimales)

       y = y + f(t, y)*h                 #on calcula nouvelle valeur de y
       y_list.append(round(y,digits))    #on ajoute le nouveau y à la fin de la liste des y

    return t_list, y_list


def euler_vect(F, Y0, t0, T, h):
    """
    Résolution d'une EDO 1D par la méthoe d'Euler explicite sous forme vectorielle.
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

    t_list = [t0]                                       #initialisation d'une liste avec les valeurs de t
    Y_list = [Y0]                                       #initialisation d'une liste avec les valeurs de y
    t = t0                                              #initialisation de t à t0, la borne inf de l'intervalle de résolution
    Y = Y0                                              #initialisation de y à y0, la condition initiale

    while t < T:                                        #Tant que la date t est inférieure à la date T
        t = t + h                                       #on incrémente la date avec le pas de calcul h
        t_list.append(t)                                #on ajoute cette nouvelle date à la fin de la liste des dates (round = arrondi à "digits" décimales)

        Y = [ y + yp * h for y, yp in zip(Y, F(t, Y)) ] #on calcula nouvelle valeur de y
        Y_list.append(Y)                                #on ajoute le nouveau Y à la fin de la liste des y

    return t_list, [Y_list[i][1] for i in range(len(Y_list))]


def runge_kutta_4(f, y0, t0, T, h, digits=10) :
    """
    Résolution d'une EDO 1D par la méthoe de RK4.
    (RAPPEL Schéma d'Euler : y_i1 = y_i + h/6*(k1+2*k2+2*k3+k4)
    où :
    k1=f(t_i,y_i)
    k2=f(t_i+h/2,y_i+k1*h/2)
    k3=f(t_i+h/2,y_i+k2*h/2)
    k4=f(t_i+h,y_i+h*k3))
    
    Paramètres
    ----------
    f  :    fonction du problème de Cauchy associé (valeur de f')
    y0 :    valeur de la condition initiale
    t0 :    valeur de la date t0 (borne inf de l'intervalle de résolution)
    T  :    valeur de la date T (borne sup de l'intevalle de résolution')
    h  :    valeur du pas h
    k1, k2, k3, k4 : coefficients de la méthode de RK4
    digits :(optionel) nombre de décimales des arrondis, 10 par défaut

    Renvoi
    -------
    t_list : liste des valeurs de t
    y_list : liste des valeurs de y correspondantes calculées par le schéma

    """
    t_list = [t0]                        #initialisation d'une liste avec les valeurs de t
    y_list = [y0]                        #initialisation d'une liste avec les valeurs de y
    t = t0                               #initialisation de t à t0, la borne inf de l'intervalle de résolution
    y = y0                               #initialisation de y à y0, la condition initiale

    while t < T:                         #Tant que la date t est inférieure à la date T
       t = t + h                         #on incrémente la date avec le pas de calcul h
       t_list.append(round(t,digits))    #on ajoute cette nouvelle date à la fin de la liste des dates (round = arrondi à "digits" décimales)

       k1=f(t,y)                         #on calcule à chaque fois les coefficients k1, k2, k3, k4 pour la méthode RK4
       k2=f(t+h/2,y+k1*h/2)
       k3=f(t+h/2,y+k2*h/2)
       k4=f(t+h,y+h*k3)
       
       y = y + h/6*(k1+2*k2+2*k3+k4)     #on calcule la nouvelle valeur de y
       y_list.append(round(y,digits))    #on ajoute le nouveau y à la fin de la liste des y

    return t_list, y_list

    


    
    
