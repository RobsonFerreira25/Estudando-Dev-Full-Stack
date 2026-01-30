import psycopg2

# Abrir conexão com banco de dados.
Conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="488981",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com o banco de dados aberta com sucesso!")

# Criar cursor e o metodo select.
cur = Conn.cursor()
cur.execute('''select * from public. AGENDA where id='1' ''')
registro=cur.fetchone()
print(registro)

# Sempre nessa ordem commit, print, close
Conn.commit()
print("Seleção realizada com sucesso!")
Conn.close()
