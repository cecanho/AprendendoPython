# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 046
# Data: 26-02-2023
# Objetivo: OO em Python - Herança

class Pessoa:
    def __init__(self, nome, endereco, cpf, telefone, celular, email):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._telefone = telefone
        self._celular = celular
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, celular):
        self._celular = celular

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email