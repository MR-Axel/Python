#Axel Rosso

import random

def tirar(dados_restantes):
    tirada=[]
    for i in range(dados_restantes):
        tirada.append(random.randint(1,6))
    return tirada


def es_generala(tirada):
    # first = tirada[0]
    # for d in tirada:
    #     if d != first:
    #         return False
    return (tirada.count(tirada[0]) == 5)


def probabilidad_una ():
    N = int(input('Ingrese la cantidad de tiradas a evaluar: '))
    G = sum([es_generala(tirar(5)) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


def lanzar_tres():
    n = 5
    tiradas_realizadas = 0
    numero = 0
    cant_max = 0
    tiradas_totales = 0
    while ((n != 0) & (tiradas_realizadas < 3)):
        guardado = [0]*6    #creo una lista de longitud de dados a tirar, cada posición 'i' representa el valor (i=0 es el valor 1 del dado, i=1 es el valor 2 del dado)
        tirada = tirar(n)   #Hago una nueva tirada de n dados
        #tiradas_totales += 1
        if (tiradas_realizadas == 0) & es_generala(tirada):
            return True

        for i in range(1, 7): #Recorro los valores del dado (1 al 6)
            for valor in tirada:
                if valor == i:
                    guardado[i-1] += 1  #Si el valor i está en la tirada, incremento esa posición de guardado

        nueva_cant_max = max(guardado)  #Si tiene el valor 1, significa que tengo escalera (guardado = [1, 1, 1, 1, 1, 0] => tirada = [1, 2, 3, 4, 5])
        nuevo_numero = guardado.index(nueva_cant_max) + 1

        if (tiradas_realizadas == 0) & (nueva_cant_max > 1): #Si estoy en la primera tirada y el máximo es mayor a 1 (ya que sirve más tirar todo de nuevo)
            cant_max = nueva_cant_max    #Obtengo la máxima cantidad de repeticiones, para quitar esa cantidad de dados en la próxima tirada
            numero = nuevo_numero   #Obtengo el número que más tiradas tuvo
            n -= cant_max
        else:
            n -= guardado[numero-1]    #Para las demás jugadas, quito dados según la cantidad que tenga el index máximo obtenido en la primera tirada

        if (tiradas_realizadas == 1) & (cant_max < nueva_cant_max):
            n = 5 - nueva_cant_max
            cant_max = nueva_cant_max
            numero = nuevo_numero
            #Ej: Por si obtuve [1, 1] en la primera tirada y en la segunda [2,2,2], conviene agarrar los '2' y devolver los '1'

        if n == 0:
            return True
        tiradas_realizadas += 1
    return False


def probabilidad_tres ():
    N = int(input('Ingrese la cantidad de jugadas (de 3 lanzamientos) a evaluar: '))
    G = sum([lanzar_tres() for i in range(N)])
    prob = G/N
    print(f'Jugué {N} veces, de las cuales {G} conseguí generala.')
    print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')


def lanzar_una():
    tirada = tirar(5)
    print(f'La tirada es:\n{tirada}')
    print('Generala Servida!') if es_generala(tirada) == True else False


if __name__ == "__main__":
    ciclo = True
    while ciclo == True:
        try:
            opc = int(input("""\nElija una opción:
            1) Lanzar una vez.
            2) Calcular probabilidades de generala cada N tiradas.
            3) Calcular probabilidad de generala cada N jugadas de 3 lanzamientos (manteniendo iguales).
            4) Salir.
            """))

            lanzar_una() if (opc == 1) else False
            probabilidad_una() if (opc == 2) else False
            probabilidad_tres() if (opc == 3) else False
            ciclo = False if (opc == 4) else True
            if (not(opc in [1, 2, 3, 4])):
                print('La opción seleccionada no es válida.')

        except ValueError:
            print('La opción seleccionada no es válida.')
