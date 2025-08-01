import sqlite3

def criar_tabela():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
            preco TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_execucao(link, email, nome_loja, preco):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO execucoes (link, email, nome_loja, preco)
        VALUES (?, ?, ?, ?)
    """, (link, email, nome_loja, preco))
    conn.commit()
    conn.close()


def atualizar_preco(email: str, novo_preco: float):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE execucoes
        SET preco = ?
        WHERE email = ?
    """, (novo_preco, email))
    conn.commit()
    conn.close()

def buscar_por_email(email: str):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM execucoes WHERE email = ?
    """, (email,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

