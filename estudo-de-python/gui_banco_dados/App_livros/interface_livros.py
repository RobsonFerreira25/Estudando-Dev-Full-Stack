import tkinter as tk
from tkinter import ttk, messagebox
from crud_livros import *

#=== JANELA PRINCIPAL ===
janela = tk.Tk()
janela.title("📚 Gestão de Livros")
janela.geometry("650x400")
janela.resizable(False, False)


#=== FRAMES ===
frame_top = ttk.LabelFrame(janela, text="Cadastro de Livros", padding=10,)
frame_top.pack(fill="x", padx=10, pady=10)

frame_button = ttk.LabelFrame(janela, text="Lista de Livros", padding=10,)
frame_button.pack(fill="both", expand=True, padx=10, pady=10)


#=== CAMPOS DE ENTRADA ===
tk.Label(frame_top, text="Título:").grid(row=0, column=0, sticky="w",)
entrada_titulo = ttk.Entry(frame_top, width=30)
entrada_titulo.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Autor:").grid(row=1, column=0, sticky="w")
entrada_autor = ttk.Entry(frame_top, width=30)
entrada_autor.grid(row=1, column=1, padx=5)

tk.Label(frame_top, text="Preço:").grid(row=2, column=0, sticky="w")
entrada_preco = ttk.Entry(frame_top, width=15)
entrada_preco.grid(row=2, column=1, padx=5, sticky="w")


#=== FUNÇÕES PRINCIPAIS ===
# Atualiza a tabela Treeview com os dados do banco
def atualizar_lista():
    for item in tabela.get_children():
        tabela.delete(item)
    livros = listar_livros()
    for livro in livros:
        tabela.insert("", "end", values=livro)
            
# Adicionar um novo livro ao banco
def adicionar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    preco = entrada_preco.get()
    if not titulo or not autor or not preco:
        messagebox.showwarning("Atenção, preencha todos os campos!")
        return
    try:
        preco = float(preco)
        inserir_livro(titulo, autor, preco)
        messagebox.showinfo("Sucesso, livro cadastrado com sucesso!")
        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        atualizar_lista()
    except ValueError:
        messagebox.showerror("Error, o preço deve ser um numero valido!")
        
# Remove livro selecionado
def deletar_livro():
    item = tabela.selection()
    if not item:
        messagebox.showwarning("Atenção, selecione um livro para excluir!")
        return
    id_livro = tabela.item(item, "values")[0]
    deletar_por_id(id_livro)
    messagebox.showinfo("Sucesso, livro excluido com sucesso!")
    atualizar_lista()
    
# Edita o livro selecionado
def editar_livro():
    item = tabela.selection()
    if not item:
        messagebox.showwarning("Atenção, selecione um livro para editar!")
        return
    
    id_livro = tabela.item(item, "values")[0]
    novo_titulo = entrada_titulo.get()
    novo_autor = entrada_autor.get()
    novo_preco = entrada_preco.get()
    
    if not novo_titulo or not novo_autor or not novo_preco:
        messagebox.showwarning("Atenção, preencha todos os campos para editar!")
        return
    try:
        novo_preco = float(novo_preco)
        atualizar_livro(id_livro, novo_titulo, novo_autor, novo_preco)
        messagebox.showinfo("Sucesso, livro atualizado com sucesso!")
        atualizar_lista()
    except ValueError:
        messagebox.showerror("Error, o preço deve ser um número valido!")
        


#=== BOTÕES ===
ttk.Button(frame_top, text="Adicionar", command=adicionar_livro).grid(row=3, column=0, pady=5)
ttk.Button(frame_top, text="Editar", command=editar_livro).grid(row=3, column=1, pady=5, sticky="w")
ttk.Button(frame_top, text="Excluir", command=deletar_livro).grid(row=3, column=2, pady=5, sticky="w")
ttk.Button(frame_top, text="Atualizar Lista", command=atualizar_lista).grid(row=3, column=3, pady=5)


#=== TABELA TREEVIEW ===
colunas = ("ID", "Título", "Autor", "Preço")
tabela = ttk.Treeview(frame_button, columns=colunas, show="headings", height=10)
for col in colunas:
    tabela.heading(col, text=col)
tabela.column("ID", width=40, anchor="center")
tabela.column("Título", width=180)
tabela.column("Autor", width=140)
tabela.column("Preço", width=80, anchor="e")
    

tabela.pack(fill="both", expand=True)


#=== INICIALIZA ==
atualizar_lista()
janela.mainloop()
   