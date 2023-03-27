# from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor

# f = Funcionario()
g = Gerente('José', '222.222.222-22', 5000.0, '123-4', 0.0)
d = Diretor('Sebastião', '222.222.222-22', 5000.0, '123-4', 0.0)
print(g.get_bonificacao())
print(d.get_bonificacao())
