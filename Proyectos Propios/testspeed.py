# by Axel Rosso

import speedtest
import time
import threading
import os
import itertools
import seaborn as sns
import tkinter


# TODO: 1) Agregar matplotlib para mostrar un gráfico lineal con la velocidad de subida y bajada en el tiempo, va actualizando dentro de func live. También listado de histórico
# TODO: 2) Implementar mejor la UI con botón de Iniciar, pausar/continuar, salir, limpiar datos
# TODO: 3) Embeber el gráfico en la UI


# def ui():  #* Create the UI
#     window = tkinter.Tk()
#     window.title("Speedtest")
#     window.geometry("600x480+10+20")
#     window.mainloop()
#     loading_message = tkinter.Label(window, text="Waiting...", fg="red", font=("Helvetica", 16))
#     loading_message.place(x=60, y=50)


def plotting():
    sns.set_theme(style="darkgrid")
    sns.lineplot()


def loading():  #* Showing the loading icon
    # global listen
    while True:     #! Change to listen var to stop after N cycles
        for c in itertools.cycle(['|', '/', '-', '\\']):
            # loading_message.text ="Waiting..."+ c
            print("Waiting...",c)
            time.sleep(0.2)
            print ("\033[A                             \033[A")


def transform(value):   #* convert bit to mb
    return round(value*(1/8000000),2)


def assign():    #* Assign methods of speedtest
    st = speedtest.Speedtest()
    download = transform(st.download())
    upload = transform(st.download())
    return download, upload


def live(): #* Thread for showing the speedtest results
    # global listen
    a = 1
    while True:
        download, upload = assign()
        print ("\033[A                             \033[A")
        print(f"{a} --------------------------------------------------------------")
        print(f"Download Speed: {download} mbs")
        print(f"Upload Speed: {upload} mbs\n\n")
        a += 1
        # listen = False


def main(): #* Start of two threads
    os.system('cls')
    # ui()
    threading.Thread(target=live).start()
    threading.Thread(target=loading).start()


if __name__ == "__main__":
    # listen = True
    main ()