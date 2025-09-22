import tkinter as tk

def captura_clic(event):
    x = event.x
    y = event.y
    label_coordenadas['text'] = f'Útimo clique: x={x}, y={y}'

# Criando janela
janela = tk.Tk()
janela.title('Tratamento de eventos - captura de clique esquerdo')

# Criando o widget de rotulo
label_coordenadas = tk.Label(janela, text='Clique em qualquer lugar da janela')
label_coordenadas.pack(padx=500, pady=300)

# Ligando o evento de clique do mouse a função
janela.bind('<Button-1>', captura_clic)

# Rodando o loop principal
janela.mainloop()
