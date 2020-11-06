# ticker.py
# Axel Rosso
# -*- coding: utf-8 -*-

from vigilante import vigilar
import sys
import csv
import informe
import formato_tabla


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 2])
    return rows


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


# def filtrar_datos(filas, nombres):    #Reemplazada en el ejercicio 9.15 por una expresión generadora
#     for fila in filas:
#         if fila['nombre'] in nombres:
#             yield fila


def ticker(camion_file, log_file, fmt):
    # Elige formato
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    # filas = filtrar_datos (filas, camion)
    filas = (fila for fila in filas if fila['name'] in camion)  # Expresión generadora para obtener los datos que se encuentren en camion
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    for fila in filas:
        formateador.fila(fila.values())


def main(args):
    camion = 'Data/camion.csv'
    filas = 'Data/mercadolog.csv'
    formato = 'html'
    ticker(camion, filas, formato)
    # ticker(sys.argv[0], sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main(sys.argv)
