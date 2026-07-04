import tkinter
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Label")
janela.geometry("250x250")
janela.resizable(width=False, height=False)

texto_label = Label(janela, width=10, height=2, text = "hello world!", fg = "green", bg = "red")
texto_label.grid(row=0, column=0)

texto_label = Label(janela, width=20, height=2, text = "my label test stuff", fg = "blue", bg = "red")
texto_label.grid(row=20, column=0)

texto_label = Label(janela, width=20, height=2, text = "i hope you guys like :)", fg = "yellow", bg = "red")
texto_label.grid(row=30, column=0)

janela.configure(background='red')

janela.mainloop()