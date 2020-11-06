# busqueda_en_listas.py


# Ejercicio 3.6
def buscar_u_elemento(lista, elem):
    pos = -1
    for i, l in enumerate(lista):
        if l == elem:
            pos = i
            break
    return pos


def buscar_n_elemento(lista, elemento):
    veces = 0
    for i in lista:
        if i == elemento:
            veces += 1
    return veces


# Ejercicio 3.7
def maximo(lista):
    maxi = 0
    for i, l in enumerate(lista):
        if i == 0:
            maxi = int(l)
        if int(l) > maxi:
            maxi = int(l)
    return maxi


def minimo(lista):
    mini = 0
    for i, l in enumerate(lista):
        if i == 0:
            mini = int(l)
        if int(l) < mini:
            mini = int(l)
    return mini



n_lista = list()
n = int(input('Elementos a ingresar: '))

for i in range(0, n):
    n_lista.append(input(f'{i+1}. Ingrese valor: '))

elemento = input('\nIngrese valor a buscar: ')

pos = buscar_u_elemento(n_lista, elemento)

if pos != -1:
    veces = buscar_n_elemento(n_lista, elemento)
    print(f'{elemento} aparece por primera vez en la posición {pos} y un total de {veces} veces')
    maximoInt = maximo(n_lista)
    minimoInt = minimo(n_lista)
    print(f'\nMáximo valor de la lista es {maximoInt}, y el minimo es {minimoInt}')
else:
    print(f'\nNo se encontró el valor: {elemento}')