import tkinter as tk

def autualizar_coordenadas(event):
    x = event.x
    y = event.y
    label_coordenadas['text'] = f'Coodenadas do mouse: x={x}, y={y}'

# Criando a janela
janela = tk.Tk()
janela.title('Tratamento de eventos - coordenadas do mouse')

# Criando widget de rotulo
label_coordenadas = tk.Label(janela, text='Mova o mouse sobre a janela para ver as coordenadas')
label_coordenadas.pack(padx=500, pady=300)

# Ligando o evento de movimento do mouse a função
janela.bind('<Motion>', autualizar_coordenadas)

# Rodando o loop principal
janela.mainloop()