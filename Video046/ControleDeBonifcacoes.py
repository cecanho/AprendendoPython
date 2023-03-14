from funcionario import Funcionario


class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes = 0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        '''if(hasattr(obj, 'get_bonificacao')):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(f"Instância de {self.__class__.__name__} não implementa o método get_bonificacao()")'''
        if(isinstance(obj, Funcionario)):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print(f"Instância de {self.__class__.__name__} não implementa o método get_bonificacao()")

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes