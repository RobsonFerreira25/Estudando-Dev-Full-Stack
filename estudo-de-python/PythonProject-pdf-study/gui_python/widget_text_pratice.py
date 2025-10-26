import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Widget Text em Tkinter Pratice")

# Cria o widget Text
T = tk.Text(janela, height=10, width=50)
T.pack()

# Função para mostrar o texto inserido no widget Text
def mostrar_texto():
    texto = T.get("1.0", tk.END) # Obtém o texto do widget Text
    print(f"Conteudo do widget Text: \n{texto}")

# Botão para mostrar o texto     
tk.Button(janela, text="Mostrar Texto", command=mostrar_texto).pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
