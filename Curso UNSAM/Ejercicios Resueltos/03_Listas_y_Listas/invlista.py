# invlista.py

def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida


lista_uno = [1,2,3,4,5]
lista_dos = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']

print (invertir_lista(lista_uno))
print (invertir_lista(lista_dos))