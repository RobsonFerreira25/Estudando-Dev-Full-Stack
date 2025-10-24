import tkinter as tk

def mostrar_dados():
    print("Nome: %s \nSobrenome: %s \nIdade: %s \nSexo: %s \nEndereço: %s \nTelefone: %s" % 
          (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
    
            
# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Usuário")

# Cria os rótulos e os posiciona
tk.Label(janela, text="Nome: ").grid(row=0, column=0)
tk.Label(janela, text="Sobrenome: ").grid(row=1, column=0)
tk.Label(janela, text="Idade: ").grid(row=2, column=0)
tk.Label(janela, text="sexo: ").grid(row=0, column=2)
tk.Label(janela, text="Endereço: ").grid(row=1, column=2)
tk.Label(janela, text="Telefone: ").grid(row=2, column=2)

# Cria as entradas e as posiciona
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e3 = tk.Entry(janela)
e4 = tk.Entry(janela)
e5 = tk.Entry(janela)
e6 = tk.Entry(janela)
e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)


janela.mainloop()
