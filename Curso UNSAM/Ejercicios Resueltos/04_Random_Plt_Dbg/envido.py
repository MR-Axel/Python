#Axel Rosso

import random

VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
PALOS = ['oro', 'copa', 'espada', 'basto']


def contar_envido(mano):
    #* Cuento cuanto tengo de envido en la mano
    for palo in PALOS:
        total = 0
        mismo_palo = 0
        una_figura = False
        for carta in mano:
            if carta[1] == palo:
                mismo_palo += 1
                if (carta[0] < 8):
                    total += carta[0]
        if mismo_palo == 1:
            total = 0   #Sino, si es basto (última pos de PALOS)..
            continue    #..no se va a reiniciar el total en el caso de no tener envido
        elif mismo_palo == 2:
            return total+20
        #elif mismo_palo == 3:
        #    print('Flor!')
        #    return total+20
    return False


def repartir ():
    naipes = [(valor,palo) for valor in VALORES for palo in PALOS]
    #random.shuffle(naipes)
    mano = random.sample(naipes,k=3) #Obtener cartas
    return mano


def mostrar_mano():
    mano = repartir()
    print(f'\nMi mano es:\n {mano}')
    envido = contar_envido(mano)
    print(f'Tengo {envido}!\n') if (envido != False) else print('Sin envido :(\n')


def probabilidad ():
    #* Para evaluar la probabilidad de conseguir un determinado tanto en N manos
    tanto = 0
    while ((tanto < 20) | (tanto > 33)):
        tanto = int(input('Ingrese la cantidad de envido a evaluar: '))
        if ((tanto < 20) | (tanto > 33)):
            print('El valor no corresponde al rango posible de envido.')
    N = int(input('Ingrese la cantidad de manos a levantar: '))
    cantidad = sum([contar_envido(repartir()) for i in range(N) if contar_envido(repartir()) == tanto])
    print(f'Realicé {N} jugadas, de las cuales obtuve envido de {tanto} el {(cantidad/N)*100:.3f}% de las veces.')


if __name__ == '__main__':
    ciclo = True
    while (ciclo == True):
        try:
            opc = int(input("""\nElija una opción:
            1) Obtener mano y ver si tengo envido.
            2) Calcular probabilidades sacar un valor específico de envido en N manos.
            3) Salir.
            """))

            mostrar_mano() if (opc == 1) else False
            probabilidad() if (opc == 2) else False
            ciclo = False if (opc == 3) else True
            if (not(opc in [1, 2, 3])):
                print('La opción seleccionada no es válida.')

        except ValueError:
            print('La opción seleccionada no es válida.')