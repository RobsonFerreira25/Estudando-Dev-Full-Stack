import tkinter as tk

janela = tk.Tk()
janela.title("Widget Text em Tkinter")

T = tk.Text(janela, height=2, width=30)
T.pack()

T.insert(tk.END, "Este é um widget Text.\n com duas linhas.\n")

janela.mainloop()
