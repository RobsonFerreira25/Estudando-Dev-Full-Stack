import tkinter as tk
from tkinter import ttk

janela  = tk.Tk()
janela.title("Widget Slider em Tkinter")

def mostrar_valores():
    print(f"Vlaro do slider 1: {s1.get()}")
    print(f"Valro do slider 2: {s2.get()}")
    
s1 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
s1.pack()
s2 = ttk.Scale(janela, from_=0, to=200, orient=tk.HORIZONTAL)
s2.pack()

ttk.Button(janela, text="Mostrar Valores", command=mostrar_valores).pack()

janela.mainloop()

