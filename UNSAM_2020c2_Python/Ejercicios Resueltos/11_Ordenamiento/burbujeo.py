from colorama import Fore, Style

def ord_burbujeo(lista):
    comparaciones = 0
    vueltas = 0
    cambios = 0
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-comparaciones):
            if lista[j] > lista[j+1]:
                aux = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = aux
                cambios += 1
            vueltas += 1
        comparaciones += 1
        if cambios == 0:
            return lista, vueltas, cambios
    return lista, vueltas, cambios

#* Creo lote de pruebas
lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

ordenados = [lista_1, lista_2, lista_3, lista_4, lista_5]

#* Mando las pruebas a la función de ordenamiento y muestro resumen de resultados
for c in ordenados:
    print("\nLista sin ordenar: ", c)
    lista, vueltas, cambios = ord_burbujeo(c)
    if cambios == 0:
        print(Fore.RED + f"La lista ya está ordenada!\nNo se realizaron cambios.\nVueltas totales: {vueltas}", Style.RESET_ALL)
    else:
        print(f"Lista ordenada: {lista}\nCambios realizados: {cambios}\nVueltas totales: {vueltas}")