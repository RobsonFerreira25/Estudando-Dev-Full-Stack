import psycopg2

# Conectar com o banco de dados.
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="488981",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com o banco de dados realizada com sucesso!")

# Criar cursor e metodo Delete
cur = conn.cursor()
cur.execute('''Delete from public.AGENDA where id='2' ''')
conn.commit()
cont = cur.rowcount
print(cont, "Registro excluido com sucesso!")
print("Exclusão realizada com sucesso!")
conn.close()
