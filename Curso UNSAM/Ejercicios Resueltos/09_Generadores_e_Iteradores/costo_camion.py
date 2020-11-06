# costo_camion.py
# Axel Rosso

import informe

def costo_camion(file_name):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe.leer_camion(file_name)
    return camion.precio_total()

cuesta = costo_camion('Data/camion.csv')
print('\nTotal pagado por los cajones es: $', round(cuesta,2))