class Cliente:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._salario = salario
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def imprimir(self):
        print(f"\n{self.nome + ' ' + self.salario}")