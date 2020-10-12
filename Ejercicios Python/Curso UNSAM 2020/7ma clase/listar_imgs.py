import os
import sys

def imprimir_png(ruta):
    '''Mostrar archivos png del directorio'''
    for root, dirs, files in os.walk(ruta):
        for name in files:
            if name.endswith(".png"):
                print(name)


def main(ruta):
    imprimir_png(ruta)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            ruta = sys.argv[1]
        else:
            ruta = '.\Data\ordenar'
        main(ruta)
    except FileNotFoundError:
        print(f'No se encuentra el directorio {sys.argv}')
