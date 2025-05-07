from data.cliente_model import Cliente
from data.cliente_sql import CRIAR_TABELA, OBTER_TODOS, INSERIR_CLIENTE
from data.util import get_connection


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()


def inserir_cliente(cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_CLIENTE, (cliente.nome, cliente.cpf, cliente.email, cliente.telefone, cliente.senha))
    conn.commit()
    conn.close()


def obter_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    clientes = cursor.fetchall()
    clientes = [Cliente(id=row[0], nome=row[1], cpf=row[2], email=row[3], telefone=row[4], senha=row[5]) for row in clientes]
    conn.close()
    return clientes
