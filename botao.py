import tkinter
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.geometry("250x250")
janela.title("Botão")

global contador
contador = 0


def comando_executavel():
    print("algo engraçado!")
         
label_text = Label(janela, width= 15, height= 2, text = "Clique no botão:")
label_text.grid(row = 10, column= 10)

botao = Button(janela, command = comando_executavel, width = 10, height = 2, text = "clique aqui!", relief="flat")
botao.grid(row = 20, column = 10)


janela.mainloop()