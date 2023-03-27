from funcionario import Funcionario

class Diretor(Funcionario):
    def get_bonificacao(self):
        return self._salario * 0.20