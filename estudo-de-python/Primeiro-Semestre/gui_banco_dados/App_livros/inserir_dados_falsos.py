from db_config import conectar
from faker import Faker
import random

# Criar um instância do gerador de dados Faker
fake = Faker("pt_BR")

def inserir_dados_fakes(quantidade=10):
    conn = conectar()
    if conn:
        cur = conn.cursor()
        try:
            for _ in range(quantidade):
                titulo = fake.catch_phrase()
                autor = fake.name()
                preco = round(random.uniform(20, 150), 2)
                cur.execute('''
                    INSERT INTO livros (titulo, autor, preco)
                    VALUES (%s, %s, %s)           
                ''', (titulo, autor, preco))
                
                
            conn.commit()
            print(f"✅ {quantidade} livros fictícios inseridos com sucesso!")
        except Exception as e:
            print("❌ Erro ao inserir dados falsos:", e)


if __name__ == "__main__":
    inserir_dados_fakes(10)