# Axel Rosso

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 1
pago_extra = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    print(f"Mes {mes}:")
    if (saldo >= pago_mensual):
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado += pago_mensual
        if ((mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin)):
            total_pagado += pago_extra
            saldo -= pago_extra
            print(" Adelanta:", pago_extra)
    else:
        pago_mensual = saldo * (1 + tasa/12)
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado += pago_mensual

    print(f" Total pagado: {round(total_pagado, 2)} - Debe: {round(saldo,2)}")
    mes += 1

print(" \nTotal pagado:", round(total_pagado, 2))

