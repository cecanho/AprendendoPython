from collections.abc import Container, Sized

class Funcionario(Container, Sized):
    _dados = []

    def __contains__(self, item):
        return self._dados.__contains__(self, item)

    def __len__(self):
        return len(self._dados)

if __name__ == '__main__':
    funcionario = Funcionario()
    print(funcionario.__len__())
    print(funcionario)