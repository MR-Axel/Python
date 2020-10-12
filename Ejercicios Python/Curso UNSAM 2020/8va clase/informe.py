# informe.py
# Axel Rosso

import fileparse
import lote
import formato_tabla


def leer_camion(nom_archivo):
    '''
    Lee un archivo de lotes en un camión
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    with open(nom_archivo) as lines:
        camion_dicts = fileparse.parse_csv(lines, select=['nombre','cajones','precio'], types=[str,int,float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
        return camion

def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))


def hacer_informe(camion, precios):
    '''
    Crea una lista de tuplas (nombre, cajones, precio, cambio)
    dada una lista de lotes en un camión y un diccionario de precios nuevos.
    '''
    filas = []
    for c in camion:
        precio_orig = c.precio
        cambio = precios[c.nombre] - precio_orig
        reg = (c.nombre, c.cajones, precio_orig, cambio)
        filas.append(reg)
    return filas


def imprimir_informe(data_informe, formateador):
    '''
    Imprime adecuadamente una tabla de una lista de tuplas
    (nombre, cajones, precio, cambio).
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Elige formato
    if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    imprimir_informe(data_informe, formateador)


def main(args):
    if (len(args) < 3) | (len(args) > 4):
        raise SystemExit('Uso: %s archivo_camion archivo_precios tipo_de_formato_(opcional: txt/csv/html)' % args[0])
    elif len(args) == 4:
        informe_camion(args[1], args[2], args[3])
    else:
        informe_camion(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
