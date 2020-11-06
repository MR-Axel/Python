#plotear_temperaturas.py
#Como precondición se tuvo que haber ejecutado el archivo termometro.py con 999 mediciones

import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('Data/Temperaturas.npy')
plt.hist(temperaturas,bins=25)
plt.ylabel('Probabilidades')
plt.xlabel('Datos')
plt.show()