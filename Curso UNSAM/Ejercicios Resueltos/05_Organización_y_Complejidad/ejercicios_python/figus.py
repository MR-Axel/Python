#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:03:43 2020

@author: rgrimson
"""

import random
import numpy as np
import matplotlib.pyplot as plt
#%%

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(album):
    return 0 in album
    
def comprar_figu(figus_total):
    '''recibe el número total de figuritas que tiene el álbum 
    devuelve un número entero aleatorio que representa la figurita que nos tocó.
    '''
    return random.randint(1,figus_total)-1
    

#%%
#Ej 4.18

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total)] += 1
    return album.sum()
    
        
cuantas_figus(6)
        
#%%
# Ejercicio 4.19
figus_total = 6
n_repeticiones = 1000
l = []

for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))
    

print(f"Para llenar un album de {figus_total} figus compré en promedio {np.mean(l)} figus ({n_repeticiones} repeticiones)")
#%%
# Ejercicio 4.20
figus_total = 670
n_repeticiones = 100

l = []

for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))
    

print(f"Para llenar un album de {figus_total} figus compré en promedio {np.mean(l)} figus ({n_repeticiones} repeticiones)")
#Para llenar un album de 670 figus compré en promedio 4723.721 figus (1000 repeticiones)

#%%
#4.22
def comprar_paquete(figus_total, figus_paquete):
    p = []
    for i in range(figus_paquete):
        p.append(comprar_figu(figus_total))
    return p

#%%
figus_total = 670
figus_paquete = 5
comprar_paquete(figus_total, figus_paquete)

#%%

#Ejercicio 4.23
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
    return album.sum()/figus_paquete

#%%
# Ejercciio 4.24

figus_total = 670
n_repeticiones = 1000
figus_paquete = 5

l = []
for i in range(n_repeticiones):
    l.append(cuantos_paquetes(figus_total, figus_paquete))
    

print(f"Para llenar un album de {figus_total} figus compré en promedio {np.mean(l)} paquetes ({n_repeticiones} repeticiones)")
#Para llenar un album de 670 figus compré en promedio 951.778 paquetes (1000 repeticiones)
#%%
#4.25 proba de 850 paq o menos
L=np.array(l)
(L<=850).sum()/n_repeticiones

#%%
#Ejercicio 4.26 Histograma
plt.hist(L,bins=50)
# o, como densidad:
plt.hist(L, bins=50, density=True)

#%%
#Ejercicio 4.27
np.percentile(L,90)

#otra forma:
L.sort()
L[int(0.9*len(L))]

#%%

#Gráfico de Tomás Bossi
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
#%%

