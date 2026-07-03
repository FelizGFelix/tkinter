import tkinter
from tkinter import *
from tkinter import ttk

janela = Tk()

text = ttk.Label(text = "Hello World").place(x= 1)
janela.title("my first tkinter project!")
janela.iconbitmap("imagemdofofodoethan.jpg")
janela.geometry("700x500")
janela.wm_maxsize(width = 800, height= 600)
janela.wm_minsize(width = 600, height= 400)

janela.resizable(width= False, height= False)

janela.configure(background="light blue")

janela.mainloop()