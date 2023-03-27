# 1. Torne a classe Conta abstrata.
# 2. Torne o método atualiza() abstrato
# 3. Tente instânciar uma Conta : O que ocorre?
# 4. Agora, instancie uma ContaCorrente e uma ContaPoupanca, e teste o código chamando o
# método atualiza()
# 5. Crie uma classe chamada ContaInvestimento
# 6. Instancie uma ContaInvestimento
# 7. Não conseguimos instanciar uma ContaInvestimento que herda Conta sem implementar o
# método abstrato atualiza() . Vamos criar uma implementação dentro da classe
# ContaInvestimento
# 8. Agora teste instanciando uma ContaInvestimento e chame o método atualiza()
# 9. (Opcional) Crie um atributo tipo nas classes ContaCorrente , ContaPoupanca e
# ContaInvestimento . Faça com que o tipo também seja impresso quando usamos a função
# print()

# from conta import Conta

# c = Conta('123-4', 'José', 5000.0, 0)

from contaCorrente import CC
from contaPoupanca import CP

cc = CC('123-4', 'PF', 'José', 5000.0)
cp = CP('124-4', 'PJ', 'Manuel', 5000.0)

cc.atualiza(0.01)
cp.atualiza(0.01)

print(cc.tipo)
print(cc.saldo)
print(cp.tipo)
print(cp.saldo)

from contaInvestimento import ContaInvestimento
ci = ContaInvestimento('125-4', 'PJ', 'Maria', 6000.0)
ci.deposita(1000.0)
ci.atualiza(0.01)
print(ci.tipo)
print(ci.saldo)