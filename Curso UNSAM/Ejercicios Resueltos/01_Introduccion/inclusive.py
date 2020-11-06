# Axel Rosso

frase_t = ""
aux = ""

frase = input("Escriba la frase a traducir: \n")
palabras = frase.split()
for palabra in palabras:
    if palabra[-1].lower() == 'o':
        aux = palabra[:-1] + 'e'
    elif palabra[-2].lower() == 'o':
        aux = palabra[:-2] + 'e' + palabra[-1]
    else:
        aux = palabra
    frase_t += aux + " "

print("Traducción:", frase_t)
