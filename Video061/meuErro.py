class MeuErro(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return repr(self.valor)

if __name__ == '__main__':
    try:
        raise MeuErro(2*2)
    except MeuErro as e:
        print('Minha exceção ocorreu, valor: {}'.format(e.valor))
        raise MeuErro('oops!')