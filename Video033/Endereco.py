# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034-035-036
# Data: 21-01-2023
# Objetivo: OO em Python - Conceito de agregação - Classe Endereço

class Endereco:
    def __init__(self, numero, complemento, logradouro, bairro, cidade, uf, pais, cep):
        self.numero = numero
        self.complemento = complemento
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.pais = pais
        self.cep = cep


