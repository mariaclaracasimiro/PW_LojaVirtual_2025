CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    senha TEXT NOT NULL
);
"""

INSERIR_CLIENTE = """
INSERT INTO clientes (nome, cpf, email, telefone, senha)
VALUES (?, ?, ?, ?, ?);
"""

OBTER_TODOS = """
SELECT id, nome, cpf, email, telefone, senha FROM clientes;
"""
