# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 047
# Data: 04-03-2023
# Objetivo: OO em Python - Reescrita e Métodos

from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, endereco, cpf,
                 telefone, celular, email, funcao, salario,
                 login, senha, qtdFuncionarios):
        super().__init__(nome, endereco, cpf,
                 telefone, celular, email, funcao, salario)
        self._login = login
        self._senha = senha
        self._qtdFuncionarios = qtdFuncionarios

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def qtdFuncionarios(self):
        return self._qtdFuncionarios

    @qtdFuncionarios.setter
    def qtdFuncionarios(self, qtdFuncionarios):
        self._qtdFuncionarios = qtdFuncionarios

    def autentica(self, login, senha):
        if (self._login == login) and (self._senha == senha):
            return True
        else:
            return False

    def get_bonificacao(self):
        return super().__init__() + 1000.0