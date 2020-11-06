#larenga.py
#Axel Rosso

def pascal(n, k):
    '''
    n: fila, k: columna (>=0)
    '''
    if (k == 0) or (n == k):
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

print(pascal(3, 1))

# Si (n, k) = (2, 1) = 2  =>  2 = 1 + 1 = (1, 0) + (1, 1)
# Si (n, k) = (3, 1) = 3  =>  3 = 1 + 2 = (2, 0) + (2, 1) = (2, 0) + (1, 0) + (1, 1)