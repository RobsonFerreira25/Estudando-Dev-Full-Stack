# create_table_run.py
import traceback
import psycopg2

DB_CONFIG = {
    "database": "livrosdb",
    "user": "postgres",
    "password": "488981",
    "host": "127.0.0.1",
    "port": "5432"
}

CREATE_SQL = '''
CREATE TABLE IF NOT EXISTS public.livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);
'''

def conectar():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conectado ao PostgreSQL:", DB_CONFIG["database"], "como", DB_CONFIG["user"])
        return conn
    except Exception as e:
        print("❌ Falha na conexão com o banco de dados.")
        traceback.print_exc()
        return None

def criar_tabela():
    conn = conectar()
    if not conn:
        return False
    try:
        cur = conn.cursor()
        print("⏳ Executando CREATE TABLE ...")
        cur.execute(CREATE_SQL)
        conn.commit()
        print("✅ Comando CREATE TABLE executado e commit feito.")
        # verificar se tabela existe via query simples
        cur.execute("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = 'livros'
            ORDER BY ordinal_position;
        """)
        cols = cur.fetchall()
        if cols:
            print("📋 Estrutura da tabela 'livros':")
            for col in cols:
                print("  -", col[0], ":", col[1])
            return True
        else:
            print("⚠️ CREATE executado mas tabela 'livros' não apareceu em information_schema.")
            return False
    except Exception:
        print("❌ Erro ao criar tabela:")
        traceback.print_exc()
        return False
    finally:
        try:
            cur.close()
        except:
            pass
        conn.close()

if __name__ == "__main__":
    ok = criar_tabela()
    if ok:
        print("✅ TUDO CERTO: tabela criada/verificada.")
    else:
        print("❌ Algo falhou — veja mensagens acima e cole o erro aqui se quiser que eu analise.")
