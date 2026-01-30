from db_config import conectar

def listar_livros():
    conn = conectar()
    if conn:
        cur = conn.cursor()
        cur.execute('''
        SELECT * FROM livros ORDER BY id ASC                
    ''')
        livros = cur.fetchall()
        print("📚 Lista de livros:")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Preco: R$ {livro[3]:.2f}")
            
    cur.close()
    conn.close()
    return livros
