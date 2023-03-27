from funcionario import Funcionario

class Gerente(Funcionario):
    def get_bonificacao(self):
        return self._salario * 0.15