import sqlite3

def criar_tabela():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
            preco TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def salvar_execucao(link, telefone, nome_loja, preco):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO execucoes (link, telefone, nome_loja, preco)
        VALUES (?, ?, ?, ?)
    """, (link, telefone, nome_loja, preco))
    conn.commit()
    conn.close()


def atualizar_preco(telefone: str, novo_preco: float):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE execucoes
        SET preco = ?
        WHERE telefone = ?
    """, (novo_preco, telefone))
    conn.commit()
    conn.close()

def buscar_por_telefone(telefone: str):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM execucoes WHERE telefone = ?
    """, (telefone,))
    resultado = cursor.fetchall()
    conn.close()
    return resultado

