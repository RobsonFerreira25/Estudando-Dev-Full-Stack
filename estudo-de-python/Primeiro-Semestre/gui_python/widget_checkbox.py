import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title("Checkbutton em Tkinter")

# Função para exibir a escolha da carreira
def escolha_carreira():
    print(f"Você escolheu a carreira: {var1.get()}, {var2.get()}")

# Cria o rótulo    
ttk.Label(janela, text="Escolha sua carreira:").grid(row=0, sticky=tk.W)

# Cria os Checkbuttons
var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)

# Cria os botões
ttk.Button(janela, text="exibir Escolha", command=escolha_carreira).grid(row=3, sticky=tk.W, pady=4)
ttk.Button(janela, text="Sair", command=janela.quit).grid(row=4, sticky=tk.W, pady=4)

# Inicia o loop principal da interface gráfica
janela.mainloop()
