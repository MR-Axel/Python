# Axel Rosso

n_cadena = ""   #El código va a ir agregando la letra en este string

cadena = input("Escribí una palabra a traducir: \n")

for c in cadena:
    if c.lower() in ('a', 'e', 'i', 'o', 'u'):    #Si se encuentra una vocal, le agrega la vocal, la p y la vocal nuevamente
        n_cadena = n_cadena + c + 'p' + c
    else:
        n_cadena = n_cadena + c
    
print("Traducción:", n_cadena)