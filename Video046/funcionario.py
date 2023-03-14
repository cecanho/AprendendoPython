# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 049
# Data: 11-03-2023
# Objetivo: OO em Python - Polimorfismo

from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, cpf,
                 telefone, celular, email, funcao, salario):
        super().__init__(nome, endereco, cpf, telefone, celular, email)
        self._funcao = funcao
        self._salario = salario

    @property
    def funcao(self):
        return self._funcao

    @funcao.setter
    def funcao(self, funcao):
        self._funcao = funcao

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10