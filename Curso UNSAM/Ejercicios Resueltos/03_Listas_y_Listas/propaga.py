# propaga.py


def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

def propagar (fosf):
    flist1 = []
    flist2 = []
    flag = 0 # *Detectar fósforo encendido pasando flag a 1

    # Recorro la lista de izquierda a derecha
    for i in range(0, len(fosf)):
        f = fosf[i]
        if f == 1:
            flag = 1
        if f == -1:
            flag = 0
        if (f == 0) and (flag == 1):
            flist1.append(1)
        else:
            flist1.append(f)

    # Recorro la lista resultante de izquierda a derecha
    for i in range(len(fosf)-1, -1, -1):
        f = flist1[i]
        if f == 1:
            flag = 1
        if f == -1:
            flag = 0
        if (f == 0) and (flag == 1):
            flist2.append(1)
        else:
            flist2.append(f)
    flist2 = invertir_lista(flist2) # Invierto la lista ya que este segundo for invierte la original

    return flist2



prueba_uno = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
prueba_dos = [ 0, 0, 0, 1, 0, 0]

print(propagar(prueba_uno))
print(propagar(prueba_dos))