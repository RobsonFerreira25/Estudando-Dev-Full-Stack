import tkinter as tk

contador  = 0
def contador_Label(lblRotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
        funcao_contar()
        
        
janela = tk.Tk()
janela.title("Contador de segundos")
lblrotulo = tk.Label(janela, fg="green")
lblrotulo.pack()

contador_Label(lblrotulo)
botao = tk.Button(janela, text="Clique aqui para interromper a contagem", width=50, command=janela.destroy)
botao.pack()

janela.mainloop()
        