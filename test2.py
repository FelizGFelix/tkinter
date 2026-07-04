import tkinter
from tkinter import *
from tkinter import ttk

janela = Tk()

texto = ttk.Label(text = "Hello World!").place(x = 1, y = 1)
texto2 = ttk.Label(text = "my second tkinter program!").place(x = 1, y = 20)

janela.title("my second tkinter stuff btw")

janela.geometry("700x500")
janela.resizable(width = False, height = False)

janela.configure(background = "gray")

janela.iconbitmap("rei.jpeg")

janela.mainloop()
