from db_config import conectar

def inserir_livros(titulo, autor, preco):
    conn = conectar()
    if conn:
        cur = conn.cursor()
        try:
            cur.execute('''
                INSERT INTO livros(titulo, autor, preco)
                VALUES(%s, %s, %s)                
            ''', (titulo, autor, preco))
            
            conn.commit()
            print(f"✅ Livro '{titulo}' adicionado com sucesso!")
        except Exception as e:
            print("❌ Erro ao inserir livro:", e)
            
        finally:
            cur.close()
            conn.close()
