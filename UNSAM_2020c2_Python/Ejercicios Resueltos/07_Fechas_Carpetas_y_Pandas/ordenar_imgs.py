# ordenar_imgs.py
# Axel Rosso

import os
import sys
import datetime

def rename(ruta, destino):
    '''
    Recorro directorio y detecto imagenes *.png
    Luego modifico fecha y las renombro
    '''
    for root, dirs, files in os.walk(os.path.join(ruta,'ordenar')):
        for name in files:
            archivo = os.path.join(root, name)
            if name[-3:] == 'png':
                # print(name)
                fecha = archivo[-12:-4]
                fecha_mod = datetime.datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), day = int(fecha[6:8]))
                ts_mod = fecha_mod.timestamp()
                direccion = os.path.join(root, name)
                os.utime(direccion, (ts_mod, ts_mod))
                os.rename(direccion, direccion[:-13] + '.png')
    return os.listdir(ruta)


def new_folder(ruta, carpeta):
    '''
    Crear subdirectorio dentro de la ruta especificada
    '''
    try:
        os.mkdir(os.path.join(ruta, carpeta))
        print(f"Mostrando directorio {ruta}\n")
    except FileExistsError:
        print(f"El subdirectorio {carpeta} ya existe!\n")


def main(ruta):
    carpeta_nueva = 'imgs_procesadas'
    new_folder(ruta, carpeta_nueva)
    rename(ruta, carpeta_nueva)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            ruta = sys.argv[1]
        else:
            ruta = '.\Data\ordenar'
        main(ruta)
    except FileNotFoundError:
        print(f'No se encuentra el directorio {sys.argv}')