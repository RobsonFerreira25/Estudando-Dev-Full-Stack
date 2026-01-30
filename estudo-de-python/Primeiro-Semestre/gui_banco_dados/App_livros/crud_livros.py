from db_config import conectar

# ==============================
# 📗 CREATE - Inserir novo livro
# ==============================
def inserir_livro(titulo, autor, preco):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO livros (titulo, autor, preco)
            VALUES (%s, %s, %s)
        ''', (titulo, autor, preco))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Livro '{titulo}' inserido com sucesso!")
    except Exception as e:
        print("❌ Erro ao inserir livro:", e)


# ==============================
# 📘 READ - Listar todos os livros
# ==============================
def listar_livros():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM livros ORDER BY id ASC")
        livros = cur.fetchall()
        cur.close()
        conn.close()
        return livros
    except Exception as e:
        print("❌ Erro ao listar livros:", e)
        return []


# ==============================
# 📝 UPDATE - Atualizar livro existente
# ==============================
def atualizar_livro(id, novo_titulo, novo_autor, novo_preco):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute('''
            UPDATE livros
            SET titulo = %s, autor = %s, preco = %s
            WHERE id = %s
        ''', (novo_titulo, novo_autor, novo_preco, id))
        conn.commit()
        cur.close()
        conn.close()
        print(f"✏️ Livro ID {id} atualizado com sucesso!")
    except Exception as e:
        print("❌ Erro ao atualizar livro:", e)


# ==============================
# 🗑️ DELETE - Excluir livro por ID
# ==============================
def deletar_por_id(id):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM livros WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"🗑️ Livro ID {id} excluído com sucesso!")
    except Exception as e:
        print("❌ Erro ao deletar livro:", e)
