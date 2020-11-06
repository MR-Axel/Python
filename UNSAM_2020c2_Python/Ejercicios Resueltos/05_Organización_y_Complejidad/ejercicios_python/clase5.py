#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:32:25 2020

@author: rgrimson
"""
  
#%% Un script es un guion, las funciones permiten ordenarnos mejor.
# Las funciones permiten un Diseño Modular y Predecibilidad.
    
def leer_precios(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primer columna debe contener un nombre y la segunda un precio.
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios
  
#%%
#Docstrings
help(leer_precios)

#%%
import csv
# Argumentos por omisión
def leer_precios(nombre_archivo, debug=False):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primer columna debe contener un nombre y la segunda un precio.
    '''
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if debug:
                print(row)
            precios[row[0]] = float(row[1])
    return precios

#Si un argumento es opcional, dale un nombre.
leer_precios('precios.csv', True)
leer_precios('precios.csv', d=True)
leer_precios('precios.csv', debug=True)

#%%
# Variable locales y globales
x = valor # Variable Global

def foo():
    y = valor # Variable Local

#%%
# Variable locales y globales

nombre = 'Dave'

def saludo():
    print('Hola', nombre)  # Usa la variable global `nombre`

def cambiar_nombre():
    nombre = "Santiago"    # Asigna a... la variable local
    print('Hola', nombre) 
    

saludo()
cambiar_nombre()
saludo()
#%%

nombre = 'Dave'

def cambiar_nombre_global():
    global nombre
    nombre = 'Guido' # Cambia el valor de la variable global

saludo()
cambiar_nombre_global()
saludo()


#%%
# Pasaje de argumentos

def agrego42(items):
    items.append(42)    # Cambia el valor de items

a = [1, 2, 3]
print(a) 
agrego42(a)
print(a) 
#%%
def sumo1(x):
    x = x + 1    # Cambia el valor de x

b = 108
print(b) 
sumo1(b)
print(b) 


#%%
# Reasignar vs modificar - tipos (in)mutalbes
# Diferencia entre modificar el valor de una variable y reasignar una variable.

def reasigno_items(items):
    items = [4, 5, 6]    # Cambia el valor de items

a = [1, 2, 3]
print(a) 
reasigno_items(a)
print(a) 


#%%
# Módulos y namespaces

#import carga un modulo y lo ejecuta
import math

math.pi

import numpy as np

np.pi 

#%%

import mi_modulo

mi_modulo.pi

mi_modulo.mi_funcion(3)

from  mi_modulo import pi
#%%
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y



#%%
# 


#%%
#

#%%
#

#%%
#

#%%
#
