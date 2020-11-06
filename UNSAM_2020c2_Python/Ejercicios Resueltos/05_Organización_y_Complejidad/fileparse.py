#fileparse.py
#Axel Rosso

import csv

def parse_csv(nombre_archivo, select = None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        registros = []
        if has_headers: #*Con Encabezado
            # Lee los encabezados
            headers = next(rows)
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []

            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    row = [row[index] for index in indices]
                # Cambio los tipos si se especificó
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # Armar el diccionario
                registro = dict(zip(headers, row))
                registros.append(registro)

        else:   #*Sin encabezado
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                # Cambio los tipos si se especificó
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                registros.append(row)

    return registros

# camion = parse_csv('Data/camion.csv', select=['nombre','cajones'], types=[str, int, float])
# precios = parse_csv('Data/precios.csv', types=[str, float], has_headers=False)
# print(f"\n{camion}")
# print(f"\n{precios}\n")