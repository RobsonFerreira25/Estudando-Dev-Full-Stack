from db_config import conectar

def atualizar_preco(id_livro, novo_preco):
    conn = conectar
    if conn:
        cur = conn.cursor()
        try:
            cur.execute('''
            UPDATE livros SET preco = %s WHERE id = %s                
        ''', (novo_preco, id_livro))
            conn.commit()
            print(f"✅ Preço do livro ID {id_livro} atualizado para R$ {novo_preco:.2f}")
        except Exception as e:
            print("❌ Erro ao atualizar livro:", e)
        
        finally:
            cur.close()
            conn.close()
