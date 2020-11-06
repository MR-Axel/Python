#lote.py
# Axel Rosso

import informe


class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones*self.precio

    def vender(self, cantidad):
        self.cajones -= cantidad

    def __str__(self):
        return f'{self.nombre}-{self.cajones}-{self.precio}'

    # Used with `repr()`
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'


# camion = informe.leer_camion('Data/camion.csv')
# print(camion)
# print (camion)

manzanas = Lote('Manzana', 200, 3)
print(manzanas)
print(repr(manzanas))