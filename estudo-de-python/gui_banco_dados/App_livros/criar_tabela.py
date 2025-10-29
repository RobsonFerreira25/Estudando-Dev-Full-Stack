from db_config import conectar

def criar_tabela():
    conn = conectar
    if conn: 
        cur = conn.cursor()
        cur.execute
        ('''CREATE TABLE IF NO EXISTS livros(
            id SERIAL PRIMARY KEY, 
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL
        )
    ''')
        
    conn.commit()
    cur.close()
    conn.close()

print("✅ Tabela 'livros' criada com sucesso!")
