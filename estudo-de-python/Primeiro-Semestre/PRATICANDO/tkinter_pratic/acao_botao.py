import tkinter
from tkinter import Button

def acao_botao():
    print('Botão pressionado!')

principal = tkinter.Tk()
botao = Button(principal, text='Olá Robson', command=acao_botao)
botao.place(x=100, y=25)

principal.mainloop()
