from datetime import date


def tiempo_transcurrido (dia, mes, anio):
    return (date.today() - date(year=anio, month=mes, day=dia))


def fecha_nacimiento():
    '''Calcular segundos pasados hasta el día de hoy'''
    print("Escribí tu fecha de nacimiento!")
    dia_nacimiento = int(input("Día: "))
    mes_nacimiento = int(input("Mes: "))
    anio_nacimiento = int(input("Año: "))
    print("Segundos transcurridos: ", int((tiempo_transcurrido(dia_nacimiento, mes_nacimiento, anio_nacimiento).total_seconds())))


def dias_restantes():
    '''Calcular días restantes para determinada fecha'''
    print("Escribí fecha de evento")
    dia_evento = int(input("Día: "))
    mes_evento = int(input("Mes: "))
    anio_evento = int(input("Año: "))
    print("Días que faltan: ", abs(tiempo_transcurrido(dia_evento, mes_evento, anio_evento)))


if __name__ == "__main__":
    opc = int(input("Elija la opción deseada: \n 1) Calcular segundos vividos.\n 2) Calcular días restantes."))
    if opc == 1:
        fecha_nacimiento()
    elif opc == 2:
        dias_restantes()