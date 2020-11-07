#By Ax
#Password generator

import string
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def generate_pass():
    printable = f'{letter}{num}{punt}'
    try:
        random_pass = random.choices(printable, k = int(combopass.get()))
        random_pass = ''.join(random_pass)
        password.set(random_pass)
        copypass["state"] = "ENABLE"
    except:
        messagebox.showinfo(
            message="El valor ingresado es incorrecto.",
            title="Error")


def copy_to_clip ():
    root.clipboard_clear()
    root.clipboard_append(password.get())
    messagebox.showinfo(
    message="The password was copied to the clipboard!",
    title="Info")


#*Base
letter = string.ascii_letters
num = string.digits
punt = string.punctuation

root = Tk()
root.geometry("320x100")
root.config(bg="black")
root.title("Password Generator")
frame = Frame(root, bg = "black")
frame2 = Frame(root, bg = "black")

#*Labels
labeltam = Label(frame, text = "Size:",
bg = "black", fg = "white")
labelpass = Label(frame, text = "Password:",
bg = "black", fg = "white")

#*List
listar_tamanio = StringVar()
listar_tamanio.set("8")
combopass = ttk.Combobox(frame, textvariable = listar_tamanio, width = 22)
combopass['values'] = [i for i in range(6,21)]

#*Entry
password = StringVar()
password.set("Press Generate...")
entrypass = ttk.Label(frame, state = "readonly", textvariable = password, width = 25)

#*Copy button
copypass = ttk.Button(frame, text = "Copy", width = 5, state = DISABLED, command = copy_to_clip)

#*Button Generate
btngrate = ttk.Button(frame2, text = "Generate!", command = generate_pass)

#*Grids positions
labeltam.grid(row = 0, column = 1, pady = 7, padx = 10)
labelpass.grid(row = 1, column = 1, pady = 7, padx = 15)
entrypass.grid(row = 1, column = 2, padx = 10)
copypass.grid(row = 1, column = 3)
combopass.grid(row = 0, column = 2, padx = 10)
btngrate.grid(row = 2, column = 1)

frame.pack()
frame2.pack(side = BOTTOM)

root.mainloop()