import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label

def acao_botao():
    print('Botao pressionado!')

'''
A janela principal recebe o modulo tkinter e a classe Tk.
'''
principal = tkinter.Tk()
# Aqui vai o codigo da interface

# Criação do botão
botao = Button(principal, text='Olá, Robson!', command=acao_botao)
botao.grid(row=0, column=2)

texto = Entry(principal)
texto.grid(row=0, column=1)

etiquta = Label(principal, text='Label')
etiquta.grid(row=0, column=0)

principal.mainloop()


