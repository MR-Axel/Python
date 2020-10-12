from prettydebug import info_debug_bl, info_debug_bl_header


def donde_insertar_lineal(lista, x, verbose = True):
    '''Insertar ordenado lineal
    Precondición: la lista está ordenada
    Poscondición: devuelve la posicion donde insertar x para que
    lista siga ordenada'''


    if verbose:
        info_debug_bl_header(lista, x)

    pos = len(lista)
    for idx, elem in enumerate(lista):



        if verbose:
            info_debug_bl(lista, idx, pos)

        if elem>=x:
            pos = idx
            break

    return pos
