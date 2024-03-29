class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def imprimir(self):
        print(f"\n{self.nome + ' ' + self.sobrenome}")

if __name__ == '__main__':
    cliente = Cliente('Cristiano', 'J. Cecanho', '123.123.123-12')
    print(cliente.nome)
    cliente.imprimir()