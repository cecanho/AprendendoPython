from conta import Conta
from contaCorrente import CC
from contaPoupanca import CP
from atualizadorDeContas import AtualizadorDeContas
from banco import Banco

# 1. Na 'main', vamos criar algumas contas e rodá-las a partir do AtualizadorDeContas
c = Conta('123-4', 'João', 1200, 1000.0)
'''cnt.extrato()'''
cc = CC('123-5', 'José', 1200, 1000.0)
'''cnt.extrato()'''
cp = CP('123-6', 'Maria', 1200, 1000.0)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c.saldo)
print(cc.saldo)
print(cp.saldo)
print()
print(cc)

atc = AtualizadorDeContas(0.1375)
'''atc.roda(cc)
atc.roda(c)
atc.roda(cp)'''

# 2. (opcional) Se você precisasse criar uma classe ContaInvestimento, e seu método atualiza()
# fosse complicadíssimo, você precisaria alterar a classe AtualizadorDeContas?
#    Não, porque retornamos o valor do resultado da conta

# 3. (opcional, Trabalhoso) Crie uma classe Banco que possui uma lista de contas. Repare que em uma
# lista de contas você pode colocar tanto ContaCorrente quanto ContaPoupanca . Crie um método
# adiciona() que adiciona uma conta na lista de contas; um método pegaConta() que devolve a
# conta em determinada posição da lista e outro pegaTotalDeContas() que retorna o total de contas
# na lista. Depois teste criando diversas contas, insira-as no Banco e depois, com um laço for ,
# percorra todas as contas do Banco para passá-las como argumento para o método roda() do
# AtualizadorDeConta

banco = Banco()
banco.adiciona(c)
banco.adiciona(cc)
banco.adiciona(cp)
for b in banco._lista_contas:
    atc.roda(b)

print(f"Saldo total: {atc.saldo_total}")

banco.pegaConta('123-5')
print(f"O total de contas da lista é: {banco.totalDeContas}")

# 4. (opcional) Que maneira poderíamos implementar o método atualiza() nas classes
# ContaCorrente e ContaPoupança poupando reescrita de código?
# Usando polimorfismo

# 5. (opcional) E se criarmos uma classe que não é filha de Conta e tentar passar uma instância no
# método roda de AtualizadorDeContas ? Com o que aprendemos até aqui, como podemos evitar
# que erros aconteçam nestes casos? Utilizando os métodos isinstance(), ou hasattr()