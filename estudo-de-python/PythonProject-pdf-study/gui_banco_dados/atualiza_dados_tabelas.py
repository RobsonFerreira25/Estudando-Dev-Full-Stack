import psycopg2

# Conectar com o banco de dados.
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="488981",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com banco de dados realizada com sucesso!")

# Consultar antes da atualização.
cur = conn.cursor()
print("Consulta antes da atualização")
cur.execute('''select * from public.AGENDA where id='1' ''')
registro = cur.fetchone()
print(registro)

# Atualização de um unico registro.
cur.execute('''Update public.AGENDA set telefone='011954542525' where id='1' ''')
conn.commit()
print("registro atualizado com sucesso!")

# Consulta depois da atualização.
cur = conn.cursor()
print("Consulta depois da atualização")
cur.execute('''select * from public.AGENDA where id='1' ''')
registro = cur.fetchone()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!")
conn.close()
