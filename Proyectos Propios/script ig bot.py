from instabot import Bot
from tkinter import filedialog
from tkinter import *
from tkinter import ttk


def login():
    username = input("Escribí tu usuario:")
    password = input("Escribí tu contraseña:")
    bot.login(password=password, username=username)


def one_directory():
    root.directory = filedialog.askdirectory(initialdir = "./",title = "Select folder")
    if root.filename == "":
        main()
    else:
        descrip = input("Escribí la descripción para el pie de foto:")
        return descrip, root.filename


def one_file():
    root.filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("images","*.jpg *.jpeg *.png"),("all files","*.*")))
    if root.filename == "":
        main()
    else:
        descrip = input("Escribí la descripción para el pie de foto:")
        return descrip, root.filename


def carga():
    temp = FALSE
    while temp == FALSE:
        select_upload = input("\nWhat do you want to upload: \n  a) One file.\n  b) An entire directory of photos.\n")
        if select_upload == "a":
            descrip, root.filename = one_file()
            temp = TRUE
        elif select_upload == "b":
            descrip, root.filename = one_directory()
            temp = TRUE
        else:
            print("Choose a valid option.")
    print(descrip)
    print(root.filename)
    bot.upload_photo(caption=descrip, photo=root.filename)


def main():
    root.title("Instaumation")
    root.geometry('250x120')
    root.configure(background = "black");
    username = Label(root ,text = "Username", bg="black", fg="white").grid(row = 0,column = 0)
    password = Label(root ,text = "Password", bg="black", fg="white").grid(row = 1,column = 0)
    username1 = Entry(root).grid(row = 0,column = 1)
    password1 = Entry(root).grid(row = 1,column = 1)
    btn_login = ttk.Button(root ,text="Login").grid(row=4,column=0)
    root.mainloop()
    #login()
    carga()


if __name__ == '__main__':
    bot = Bot()
    root = Tk()
    main()

#TODO   Preguntar si se desea añadir una descripción a cada una de las fotos del folder. Si acepta, recorrer con un for la misma cantidad de fotos seleccionadas y pedir descripción para cada "xxx.jpg"
#TODO   Acomodar la selección por folder, para que recorra toda la carpeta armando una lista de strings con paths
#TODO   Luego, con un for recorrer esa lista e ir cargando a instagram todas las fotos seleccionadas con la lista de descripciones si corresponde
#TODO   Acomodar GUI