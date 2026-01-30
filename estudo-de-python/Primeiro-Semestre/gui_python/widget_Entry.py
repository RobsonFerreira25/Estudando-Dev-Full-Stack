import tkinter as tk

def mostrar_nomes():
    print("nome: %s \nSobrenome: %s" % (e1.get(), e2.get()))
    
# Cria a janela principal
janela = tk.Tk()
janela.title("Aplicação GUI com Entry")


# Cria e posiciona os rótulos
tk.Label(janela, text="Nome: ").grid(row=0)
tk.Label(janela, text="Sobrenome:").grid(row=1)

# Cria e posiciona os campos de entrada
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# Cria e posiciona o botão
tk.Button(janela, text="Sair", command=janela.quit).grid(row=3, column=0, sticky=tk.W, pady=4, padx=15)
tk.Button(janela, text="Exubir Dados", command=mostrar_nomes).grid(row=3, column=1, sticky=tk.W, pady=4, padx=15)


janela.mainloop()
