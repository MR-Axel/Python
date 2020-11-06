# Axel Rosso

import math

r = float(input("Ingresá el radio de la esfera \n"))
volumen = 4/3 * math.pi * pow(r,3)              # También puede ser r**3
print("El volumen es: ", str(round(volumen,2)))

