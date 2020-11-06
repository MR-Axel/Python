from prettydebug import info_debug_bl, info_debug_bl_header


def busqueda_lineal_v2(lista, x, verbose = True):
    '''Búsqueda lineal ordenada
    Precondición: la lista está ordenada
    Poscondición:
      - devuelve p tal que lista[p] == x, si x está en lista;
      - devuelve -1 si x no está en lista'''

    if verbose:
        info_debug_bl_header(lista, x)

    pos = -1
    for idx, elem in enumerate(lista):
        if elem==x:
            pos = idx

        if verbose:
            info_debug_bl(lista, idx, pos)

        if elem>=x:

            break

    return pos


lista_ejemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
lista_2 = [0,2,4,6]
