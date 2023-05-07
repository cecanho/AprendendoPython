from _collections_abc import Container

class Funcionario(Container):
    def __contains__(self, item):
        return self._dados.__contains__(self, item)

if __name__ == '__main__':
    funcionario = Funcionario()