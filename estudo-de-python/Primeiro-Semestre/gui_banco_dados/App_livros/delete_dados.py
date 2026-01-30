from db_config import conectar

def excluir_livro(id_livro):
    conn = conectar
    if conn:
        cur = conn.cursor()
        try:
            cur.execute('''
            DELETE FROM livros WHERE id = %s                
        ''', (id_livro,))
            conn.commit()
            print(f"✅ Livro ID {id_livro} excluído com sucesso!")
        except Exception as e:
            print("❌ Erro ao excluir livro:", e)

        finally:
            cur.close()
            conn.close()
