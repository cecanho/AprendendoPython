# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034-035
# Data: 21-01-2023
# Objetivo: OO em Python - Conceito de agregação

class ClientePF:
    def __init__(self, nome, sobrenome, cpf, rg, endereco, telefone, celular, telefoneContato):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone
        self.celular = celular
        self.telefoneContato = telefoneContato
