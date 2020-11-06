def valor_absoluto(n):
    '''
    Obtener el valor absoluto de n
    ------------
    Precondición: n ingresado es real
    Poscondición: n devuelto es positivo
    '''
    if n >= 0:
        return n
    else:
        return -n

#*--------------------------------------------------------

def suma_pares(l):
    '''
    Realiza la suma de números pares de una lista
    ------------
    Precondición: la lista posee números reales en la lista
    Poscondición: devuelve la suma de números pares
    '''
    res = 0 #!invariante antes de comenzar el ciclo
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res

#*--------------------------------------------------------

def veces(a, b):
    '''
    Multiplicación de dos números, a y b
    ------------
    Precondición: a debe ser real, y b un entero
    Poscondición: producto entre a y b
    '''
    res = 0 #!invariantes antes de comenzar el ciclo
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

#*--------------------------------------------------------

def collatz(n):
    '''
    Funcion de conjetura de Collatz
    ------------
    Precondición: n debe ser un entero positivo
    Poscondición: n se divide por 2 al ser par,
                o sino realiza la operación 3*n+1
    '''
    res = 1 #!invariante antes de comenzar el ciclo

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res