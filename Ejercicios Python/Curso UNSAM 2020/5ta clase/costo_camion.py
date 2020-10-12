# costo_camion.py
# Axel Rosso

import informe_funciones as informe

def costo_camion(file_name):
    costo = 0
    rows = informe.leer_camion(file_name)
    for i, row in enumerate(rows, start=1):
        try: # Si no hay datos faltantes, hace la cuenta
            Ncajones = row['cajones']
            Precio = row['precio']
            costo += Ncajones * Precio
        except ValueError: # Si faltan datos, tirame un warning
            print(f'Fila {i}: No se puede interpretar: {row}')
    return (costo)
cuesta = costo_camion('Data/camion.csv')
print('\nTotal pagado por los cajones es: $', round(cuesta,2))