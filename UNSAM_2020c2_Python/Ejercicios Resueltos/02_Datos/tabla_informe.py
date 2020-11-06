#informe.py
#Axel Rosso

import csv
import sys
from pprint import pprint


def leer_precios(archivo_precios):
    precios = []
    with open(archivo_precios, 'rt') as f:
        rows_c = csv.reader(f)
        header = ['Producto', 'Precio']
        for i, line in enumerate(rows_c):
            try:
                precio = dict(zip(header,line))
                precios.append(precio)
            except IndexError:
                print(f'Error en línea {i}: No se pudo interpretar {line}')
    return precios


def leer_camion(nombre_archivo):
    camiones = []
    with open(nombre_archivo, 'rt') as f:
        rows_c = csv.reader(f)
        header = next(rows_c)
        for i, line in enumerate(rows_c):
            try:
                camion = dict(zip(header,line))
                camiones.append(camion)
            except IndexError:
                print(f'Error en línea {i}: No se pudo interpretar {line}') #! Debe mostrar la línea
    return camiones


def precio_ventas(camion, precios):
    total = 0
    venta = 0
    for carga in camion:
        total += int(carga['cajones'])*float(carga['precio'])
        for i, precio in enumerate(precios):
            try:
                if precio['Producto'] == carga['nombre']:
                    venta += int(carga['cajones']) * float(precio['Precio'])
            except KeyError:
                print(f'Error de lectura en línea {i}: {precio}')
    print(f'\nTotal camión: ${total}')
    print('Coste del camion: $', round(venta-total, 2))
    print(f'Ganancia del vendedor: ${venta}')


def hacer_informe(camion, precios):
    informe = []
    for carga in camion:
        for precio in precios:
            try:
                if precio['Producto'] == carga['nombre']:
                    data = (carga['nombre'],    #nombre de producto
                            int(carga['cajones']),  #cantidad
                            round(float(carga['precio']),2),    #precio
                            round(float(precio['Precio']) - float(carga['precio']), 2) #cambio
                            )
                    informe.append(data)
            except KeyError:
                continue
    return informe


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            nombre_archivo = sys.argv[1]
        else:
            nombre_archivo = 'Data/camion.csv'
        archivo_precios = 'Data/precios.csv'
        precios = leer_precios(archivo_precios)
        camion = leer_camion(nombre_archivo)
        pprint(precios)
        print('\n')
        pprint (camion)
        print('\n')
        precio_ventas(camion, precios)
        informe = hacer_informe(camion, precios)
        head = ("Nombre", "Cajones", "Precio", "Cambio")
        print(f'{head[0]:^10s} {head[1]:^10s} {head[2]:^10s} {head[3]:^10s}')
        print("---------- ---------- ---------- ----------")
        for r in informe:
            r = (r[0], r[1], '$'+str(r[2]), r[3])
            print(f'{r[0]:<10s} {r[1]:^10d} {r[2]:^10s} {r[3]:^10.2f}')
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv}')
