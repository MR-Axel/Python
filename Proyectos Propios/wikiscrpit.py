import wikipedia
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

def details(word):
    global results1
    try:
        result=wikipedia.summary(word)
        results1.config(text=result)
    except:
        results1.config(text="Word not found, gil")


def main():
    root.title("Wachipedia")
    root.geometry('500x400')
    root.configure(background = "black");
    word = Label(root ,text = "Search...", bg="black", fg="white").grid(row = 0,column = 0)
    results = Label(root ,text = "Password", bg="black", fg="white").grid(row = 1,column = 0)
    word1 = Entry(root).grid(row = 0,column = 1)
    results1 = Label(root)
    btn_search = ttk.Button(root, text="Search", command=details(word)).grid(row=4,column=0)
    root.mainloop()
    word = input("Search: ")


if __name__ == '__main__':
    root = Tk()
    main()