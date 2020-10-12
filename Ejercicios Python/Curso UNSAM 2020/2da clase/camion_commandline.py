# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    grand_total = 0
    with open (nombre_archivo, 'rt') as f:
        headers = next(f).split(',')
        print ('\nArchivo {}:\nCon cabecera: {}\n'.format(nombre_archivo, headers))
        for line in f:
            row = line.split(',')
            try:
                total = float(row[2]) * float(row[1])
            except ValueError:
                print(f'{row[0]} posee un error:', end = '')
                total = 0
            finally:
                grand_total += total
                print('{} cajones de {} a ${} c/u. Total: ${}'.format(row[1],row[0], float(row[2]), round(total,2)))
    return grand_total

try:
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = 'Data/camion.csv'

    costo = costo_camion(nombre_archivo)
    print(f'''_______________________________________________________
Gran Total: ${costo}\n
    ''')
except FileNotFoundError:
    print(f'No se encuentra el archivo {sys.argv}')