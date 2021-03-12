# -*- coding: utf-8 -*-
"""
Contient les fonctions de résolution à plusieurs dimensions :
    - 
"""
import numpy as np
import schemas_1d 

def solution_dim_2(g, y0, yp0, t0, T, h):
    
    # y   = y0                    # y
    # yp  = yp0                   # y'
    # ypp = g(t0, y0,  yp0)       # y"
    
    # Y0  = np.array(y0, u0)      # Y0
    # Y   = np.array(y, yp)       # Y
    # Yp  = np.array(yp, ypp)     # Y'
    
    Y0  = (y0, yp0)      # Y0
    
    def F(t, Y):
        yp  = Y[1]
        ypp = g(t, Y[0], Y[1])
        return [yp, ypp]
    # F = lambda t, Y: Y[1], g(t, Y[0], Y[1])
    
    t_list, Y_list = schemas_1d.euler_vect(F, Y0, t0, T, h)


    return t_list, Y_list


g = lambda t, y, yp : -yp
x, y = solution_dim_2(g, 1, 1, 0, 10, 0.1)
import traces
traces.trace(x, y)