#Axel Rosso

import random
import numpy as np
import matplotlib.pyplot as plt
from statistics import median
N = 999


def campana(maxi, mini, veces, total, l_mediana):
    mediciones = []
    for i in range(6):
        medicion = float(random.normalvariate(0,0.2))
        veces += 1
        mediciones.append(round(medicion, 3))
        #!(0, 1) = (mu, sigma) = (media, desvío estándar)
        np.save('Data/Temperaturas.npy', mediciones)
    total += sum(mediciones)
    n_maxi = max(mediciones)
    n_mini = min(mediciones)
    l_mediana.append(median(sorted(mediciones)))
    if n_maxi > maxi:
        maxi = n_maxi
    if n_mini < mini:
        mini = n_mini
    print(f'{mediciones}')
    return maxi, mini, veces, total, l_mediana

def graficar ():
    mediciones = np.load('Data/Temperaturas.npy')
    plt.hist(mediciones, bins=25)

if __name__ == '__main__':
    ciclo = True
    while ciclo == True:
        try:
            opc = int(input("""\nElija una opción:
            1) Realizar mediciones.
            2) Graficar mediciones
            3) Salir
            """))
            if opc == 1:
                maxi, mini, veces, total = 0, 0, 0, 0
                l_mediana = []
                for i in range(N):
                    maxi, mini, veces, total, l_mediana = campana(maxi, mini, veces, total, l_mediana)
                print(f'''En {N} veces ejecutadas la Campana con 6 valores resultantes, obtuve:
                Máximo: {maxi}.
                Mínimo: {mini}.
                Promedio: {total/N:.3f}.
                Mediana: {median(sorted(l_mediana)):.3f}.
                ''')
            if opc == 2:
                graficar()
            ciclo = False if (opc == 3) else True
            if (not(opc in [1, 2, 3])):
                print('La opción seleccionada no es válida.')
        except ValueError:
            print('La opción seleccionada no es válida.')
