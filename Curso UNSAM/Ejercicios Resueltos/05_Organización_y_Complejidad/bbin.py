# bbin.py
# Axel Rosso

def insertar(lista, x):
    lista.append(x)
    lista = sorted(lista)
    return lista


def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if pos != -1:
        print("La posición de {} es: {}\n".format(x, pos))
        print(f"Lista ordenada: {lista_ordenada}")
        return pos
    else:
        print(f"No se encontró el elemento {x}")
        print("Nueva lista: ", insertar(lista, x))
        return medio if (lista[medio] > x) else (medio + 1)


if __name__ == '__main__':
    lista_ordenada = []
    lista_no_ordenada = []
    cantidad = int(input("\nCantidad de elementos a agregar: "))
    for i in range(0, cantidad):
        lista_no_ordenada.append(int(input(f"Elemento {i+1}: ")))
    print(f"\nLista NO ordenada: {lista_no_ordenada}")
    lista_ordenada = sorted(lista_no_ordenada)
    print(f"Lista ordenada: {lista_ordenada}")
    elemento = int(input("\nIngrese valor a buscar: "))
    donde_insertar(lista_ordenada, elemento, verbose=True)