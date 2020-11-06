import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    GRAY = '\033[90m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def lista_a_str(l):
    return " ".join([str(x) for x in l])

iteracion = 0

def reset_contador():
    global iteracion
    iteracion = 0

def info_debug_bl_header(lista, x):
    print(f'                 Buscando: {x}')
    print(f'[DBG] itr idx pos Índices: ' +
                " ".join([f'{i:^3d}' for i in range(len(lista))]))
    reset_contador()


def info_debug_bl(lista, i, pos, wait=1):
    global iteracion
    str_res = ""
    for idx,elem in enumerate(lista):
        if idx < i:
            str_res += bcolors.GRAY + f'{elem:^3d}' + bcolors.ENDC
        elif idx == i:
            str_res += (bcolors.FAIL + bcolors.BOLD +
                        f'{elem:^3d}' + bcolors.ENDC +  bcolors.ENDC)
        else:
            str_res += bcolors.OKGREEN + f'{elem:^3d}' + bcolors.ENDC

        str_res += " "

    print(f'[DBG] {iteracion:^3d} {i:^3d} {pos:^3d} Mirando: {str_res}')
    time.sleep(wait)
    iteracion += 1


def info_debug_bb_header(lista, x):
    print(f'                   Buscando: {x}')
    print(f'[DBG]itr izq|med|der pos idx: ' +
                " ".join([f'{i:^3d}' for i in range(len(lista))]))
    reset_contador()



def info_debug_bb(lista, i, m, d, pos, wait=1):
    global iteracion
    str_res = ""
    for idx,elem in enumerate(lista):
        if idx < i or idx>d:
            str_res += bcolors.GRAY + f'{elem:^3d}' + bcolors.ENDC
        elif idx == m:
            str_res += (bcolors.FAIL + bcolors.BOLD +
                        f'{elem:^3d}' + bcolors.ENDC +  bcolors.ENDC)
        else:
            str_res += bcolors.OKGREEN + f'{elem:^3d}' + bcolors.ENDC

        str_res += " "

    print(f'[DBG]{iteracion:^3d} {i:^3d}|{m:^3d}|{d:^3d} {pos:^3d} lis: {str_res}')
    time.sleep(wait)
    iteracion += 1

