from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    email: str
    telefone: str
    senha: str

    