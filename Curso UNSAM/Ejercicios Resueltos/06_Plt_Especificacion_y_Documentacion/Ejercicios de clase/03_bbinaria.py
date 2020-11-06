from prettydebug import info_debug_bb, info_debug_bb_header


def busqueda_binaria(lista, x, verbose = True):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Poscondición:
      - devuelve p tal que lista[p] == x, si x está en lista;
      - devuelve -1 si x no está en lista'''

    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    if verbose:
        info_debug_bb_header(lista, x)
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
           #
        if verbose:
            info_debug_bb(lista, izq, medio, der, pos)

        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    return pos


lista_ejemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
lista_2 = [0,2,4,6]
