# soluciones_de_errores.py



#%%

# Ejercicio 3.1: Semántica

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')

#tiene_a('UNSAM 2020')
#tiene_a('abracadabra')
#tiene_a('La novela 1984 de George Orwell')

#Comentario: El error estaba en que al ingresar al 'else' devolvía falso, cortando el ciclo
#    Lo corregí sacando el false
# Entiendo que la función solamente es para comprobar la 'a' minúscula

#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))



#%%

# Ejercicio 3.2: Sintaxis

# def tiene_a(expresion)
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')

# En este ejercicio, se detectaron errores de sintaxis en:
#   1) Linea 'def tiene_a(expresion) (faltaba :)
#   2) Linea while i<n (faltaba :)
#   3) Linea if expresion[i] == 'a' (faltaba :)
#   4) return Falso (Falso no es lo mismo que False)

#Comentario: Errores encontrados:
#   1) 'def tiene_a(expresion)': Agregué los dos puntos finales
#   2) 'while i<n': Agregué los dos puntos finales
#   3) "if expresion[i] == 'a'": Agregué los dos puntos finales
#   4) return Falso: Se corrigió a False

#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))



#%%

# Ejercicio 3.3: Tipos

# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene

# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)

#Comentario: Errores encontrados:
#   1) 'tiene_uno(1984)': Se le está enviando un int, se agregaron las comillas ya que en la iteración espera un str

#    A continuación va el código corregido

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))



#%%
# Ejercicio 3.4: Alcances

# def suma(a,b):
#     c = a + b

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")


#Comentario: Faltaba devolver la var 'c'

#    A continuación va el código corregido

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")



#%%
# Ejercicio 3.5: Pisando memoria

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

# camion = leer_camion("Data/camion.csv")
# pprint(camion)

#Comentario: Se modificó el ciclo ya que se pisaban los valores, ya que indicaba siempre la misma key

#    A continuación va el código corregido

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado, (fila[0], int(fila[1]), float(fila[2]))))
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)