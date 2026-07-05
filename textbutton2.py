import tkinter
from tkinter import *
from tkinter import ttk

global contador
contador = 0
def contar():

    global contador
    print(contador)
    contador += 1

    text_label1["text"] = contador


janela = Tk()
text_label1 = Label(janela, width= 30, height= 2, text = "Clique no botão super confiavel: ")
text_label1.grid(row = 10, column = 10)

button_forlabel1 = Button (janela, command=contar, width= 20, height= 2, text = "Clique no botão super confiavel!", relief = "flat")
button_forlabel1.grid(row = 20, column= 10)

janela.mainloop()

