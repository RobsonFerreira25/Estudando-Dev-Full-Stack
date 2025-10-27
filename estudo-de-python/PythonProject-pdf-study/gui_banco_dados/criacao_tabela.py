import psycopg2

# Criando conexão com o banco de dados
conn = psycopg2.connect(database="postgres", user="postgres", password="488981", host="127.0.0.1", port="5432" )
print("Conecção com o banco de dados aberta com sucesso!")

# Criando o cursor e tabela
cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL, Nome TEXT NOT NULL, Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()