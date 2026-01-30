from faker import Faker
import psycopg2

fake = Faker("pt_BR")

conn = psycopg2.connect(
    database="lojadb",
    user="postgres",
    password="488981",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com banco de dados bem sucedida!")

cur = conn.cursor()

for _ in range(10):
    nome = fake.word()
    preco = round(fake.random_number(digits=5) / 100, 2)
    cur.execute('''
        INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)               
''', (nome, preco))
    
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()

