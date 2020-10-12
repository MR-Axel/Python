# arboles.py
# Axel Rosso

import csv
from collections import Counter


def leer_arboles(nombre_archivo):
    file = open(nombre_archivo, 'rt', encoding = "utf8")
    rows = csv.reader(file)
    header = next(rows)
    indices = [header.index(col) for col in header]
    arboleda = [{col: row[index] for col, index in zip(header, indices)} for row in rows]
    return arboleda


def leer_parque (nombre_archivo, parque_buscado):
    ''''
    Árboles del parque seleccionado
    '''
    with open(nombre_archivo, 'rt', encoding = "utf8") as f:
        parques = []
        seleccionados = []
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            parque_dict = {}
            parque_dict = dict(zip(header, row))
            if parque_dict['espacio_ve'] == parque_buscado:
                seleccionados.append(parque_dict)
            parques.append(parque_dict)
    return seleccionados


def especies(lista_arboles):
    ''''
    Listar Especies existentes
    '''
    lista_especies = []
    especie = []
    for arbol in lista_arboles:
        especie.append(arbol["nombre_com"])
    lista_especies = set(especie)   # Al ser un set, evito que se repita el valor
    return lista_especies


def contar_ejemplares(lista_arboles):
    '''
    Contador de especies existentes
    '''
    contar_especies = Counter()
    for especie in lista_arboles:
        contar_especies[especie['nombre_com']] += 1
    return contar_especies


def obtener_alturas(lista_arboles, especie):
    '''
    Alturas de determinado árbol ingresado
    '''
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


def obtener_inclinaciones(lista_arboles, especie):
    '''
    Inclinaciones de la especie seleccionada de determinado parque
    '''
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(float(arbol['inclinacio']))
    return (inclinaciones)


def especimen_mas_inclinado(lista_arboles):
    '''
    Especimen con mayor inclinación de determinado parque
    '''
    mayor = []
    es_mayor = 0
    for arbol in lista_arboles:
        if es_mayor <= float(arbol['inclinacio']):
            es_mayor = float(arbol['inclinacio'])
            especie = arbol['nombre_com']
    return mayor


def especie_promedio_mas_inclinada(lista_arboles):
    '''
    Especimen con mayor inclinación de determinado parque
    '''
    mas_inclinado = []
    especis = especies(lista_arboles)
    for tipo in especis:
        inclinado = obtener_inclinaciones(lista_arboles, tipo)
        mas_inclinado.append(round(sum(inclinado)/float(len(inclinado)),2))
    inclinaciones_dict = dict(zip(especis, mas_inclinado))
    return inclinaciones_dict


if __name__ == "__main__":
    maximo = 0
    maximos = []
    promedios = []
    inclinaciones = []
    parques = []
    print("Ingrese 3 nombres de parques:")
    for x in range(3):
        resultado = input(f"Ingrese nombre del parque {x+1}: ").upper()
        parques.append(resultado)

    especie_seleccionada = input("Escriba una especie del listado: ")

    for i in range (3):
        resultado = leer_parque('Data/arbolado-en-espacios-verdes.csv', parques[i])
        especies = especies(resultado)
        cantidad_ejemplares = contar_ejemplares(resultado)
        frecuentes = cantidad_ejemplares.most_common(5)
        parques.append(cantidad_ejemplares)

        altura = obtener_alturas(resultado, especie_seleccionada)
        maximo = max(altura)
        maximos.append(max(altura))
        promedio = round(sum(altura)/float(len(altura)),2)
        promedios.append(promedio)
        inclinaciones.append(obtener_inclinaciones(resultado, especie_seleccionada))
        mas_inclinado = especimen_mas_inclinado(resultado)
        promedio_mas_inclinado = especie_promedio_mas_inclinada(resultado)
        print(f"{maximo}\n {promedio}")
    #* Agregados de Clase 3
    arboleda = leer_arboles('Data/arbolado-en-espacios-verdes.csv')
    AltDiam = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie_seleccionada]
    # Arriba genero tipla de alturas y diámetros de determinada especie