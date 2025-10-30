import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            database="livrosdb",
            user="postgres",
            password="488981",
            host="127.0.0.1",
            port="5432"
        )
        return conexao
    except Exception as e:
        print("❌ Erro ao conectar ao banco de dados:", e)
        return None
