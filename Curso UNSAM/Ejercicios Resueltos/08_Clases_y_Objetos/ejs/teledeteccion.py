#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:40:10 2020

@author: rgrimson
"""



import numpy as np
import matplotlib.pyplot as plt

#Levanto los datos
bNIR=np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy')
bR=np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy')
bG=np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band3_clip.npy')
bB=np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band2_clip.npy')

#%%
#los veo mal
plt.imshow(bR)

#%% miro banda roja
#miro el histograma
plt.hist(bR.flatten(),bins=250)
#lo refino
plt.hist(bR.flatten(),bins=250,range=(0,3))

#%%
plt.imshow(bR,vmin=0, vmax=3)

#%%
#miro el NIR
plt.hist(bNIR.flatten(),bins=250)
#lo refino
plt.hist(bNIR.flatten(),bins=250,range=(0,5))
plt.imshow(bNIR,vmin=1, vmax=5)


#%%
#calculo NDVI y trunco potenciales problemas
ndvi = (bNIR - bR) / (bNIR+bR)
ndvi[ndvi>1]=1
ndvi[ndvi<-1]=-1

plt.hist(ndvi.flatten(),bins=250)

plt.imshow(ndvi,vmin=0,vmax=0.8)
#plt.imshow(ndvi,vmin=-1,vmax=0)
#%%
#elijo un clip pequeño para hacer las pruebas
sy = 1100
sx = 2000
dx = 600
dy = 600
clip = ndvi[sy:sy+dy, sx:sx+dx]
plt.figure(figsize=(7,7), dpi=150)
plt.imshow(clip,vmin=0,vmax=.7)

#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img_google = mpimg.imread("Data/img_google.png")
plt.figure(figsize=(7,7), dpi=150)
plt.imshow(img_google)
plt.show()


#%%

#importo el clasificador y defino una instancia para clasificar con dos etiquetas
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)

#le saco la estructura bidimensional a la matriz NDVI y la llamo datos
datos = clip.reshape(-1,1)

#entreno o ajusto el el clasificador con los datos (demora!)
kmeans.fit(datos) #ajusta el modelo
#usa el modelo ajustado para poner etiquetas
etiquetas = kmeans.predict(clip.reshape(-1,1)) 
#%%
#visualizo los resultado,s recuperando la estructura de matriz
plt.figure(figsize=(7,7), dpi=200)
plt.imshow(etiquetas.reshape(clip.shape),cmap='jet')

#%%
