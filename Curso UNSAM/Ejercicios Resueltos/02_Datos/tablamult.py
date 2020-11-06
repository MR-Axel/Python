# tablamult.py
# Axel Rosso

valores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('''     0   1   2   3   4   5   6   7   8   9
---------------------------------------------''')

for i in valores:   #Filas
    print(f"{i}",end=': ')
    for j in valores:  #Columnas
        valor = 0
        for a in range(i):  #Sumar i veces el valor
            valor += j
        print (f'{valor:>3d}',end=' ')
    print('\n')