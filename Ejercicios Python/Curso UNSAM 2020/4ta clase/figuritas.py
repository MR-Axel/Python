# figuritas.py
# Axel Rosso

import random
import numpy as np
import matplotlib.pyplot as plt


F_TOTAL = 670 # Figuritas para el álbum
F_PAQUETE = 5 # Figuritas por paquete
REPETICIONES = 100 # De Análisis
paquete = []


def crear_album():
    return np.zeros(F_TOTAL, dtype=np.int64)


def album_incompleto(A):
    return not A.all()


def comprar_figu():
    return random.randint(1,F_TOTAL)


def cuantas_figus():
    compradas = 0
    album = crear_album()
    while album_incompleto(album) == True:
        n_figu = comprar_figu()
        compradas += 1
        album[n_figu-1] += 1
    return compradas


def comprar_paquete():
    paquete = np.array([0]*F_PAQUETE) # Vector de 5 figuritas
    for i in range(F_PAQUETE-1): # 5 figuritas random
        paquete[i] = random.randint(1,F_TOTAL)
    return paquete


def cuantos_paquetes():
    cant_compras = 0
    album = crear_album() # Creo album
    while album_incompleto(album) == True:
        paquete = comprar_paquete()
        cant_compras += 1
        for i in range(F_PAQUETE-1):
            album[paquete[i]-1] += 1
    return cant_compras


def main():
    conseguidas = [cuantas_figus() for i in range(REPETICIONES)]
    promedio_figus = np.mean(conseguidas)
    en_paquete = [cuantos_paquetes() for i in range(REPETICIONES)]
    promedio_paquetes = np.mean(en_paquete)
    print(f"\nFiguritas conseguidas:\n{conseguidas}.")
    print(f"\nSe compraron {promedio_figus} figuritas en promedio.")
    print (f"Se compraron {promedio_paquetes} paquetes en promedio.")
    en_paquete850 = np.sum([1 for i in range(REPETICIONES) if cuantos_paquetes() <= 850])
    print (f"De {REPETICIONES} veces, en solo {en_paquete850:.0f} se tuvo que llegar a comprar 850 paquetes para completar el álbum.")
    print (f"La probabilidad de poder comprar hasta 850 paquetes es de {(en_paquete850/REPETICIONES)*100}%")

    plt.hist(en_paquete,bins=80)
    plt.ylabel("Probabilidad")
    plt.xlabel("Paquetes")
    plt.show()


if __name__ == "__main__":
    main()