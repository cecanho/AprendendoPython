# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 038
# Data: 29-01-2023
# Objetivo: OO em Python - Exercícios OO pag 107/114

'''
Enunciado

1. (Opcional) Crie uma classe para representar um cliente do nosso banco que deve ter nome ,
sobrenome e cpf . Instancie uma Conta e passe um cliente como titular da conta. Modifique o
método extrato() da classe Conta para imprimir, além do número e o saldo, os dados do
cliente. Podemos criar uma Conta sem um Cliente ? E um Cliente sem uma Conta ?

2. (Opcional) Crie uma classe que represente uma data, com dia, mês e ano. Crie um atributo
data_abertura na classe Conta . Crie uma nova conta e faça testes no console do Python.

3. (Desafio) Crie uma classe Historico que represente o histórico de uma Conta seguindo o
exemplo da apostila. Faça testes no console do Python criando algumas contas, fazendo operações e
por último mostrando o histórico de transações de uma Conta . Faz sentido criar um objeto do tipo
Historico sem uma Conta?
'''

from conta import Conta
from cliente import Cliente
# from pessoa import Pessoa


cride = Cliente('Cristiano', 'Cecanho', '123.123.123-12')
conta = Conta('001', cride, 300.0, 1000.0)
conta.extrato()

jose = Cliente('Jose', 'Cecanho', '123.123.123-12')
conta = Conta('001', jose, 300.0, 1000.0)
conta.extrato()
'''data = Data_Abertura()

print(data.abertura_de_conta())'''

'''cliente = Cliente('João', 'da Silva', '123.123.123-12')

conta1 = Conta('123-4', cliente, 120.0, 1000.0)
#conta2 = Conta('123-4', 'Zeca', 100.0, 1000.0)

conta1.deposita(50.0)
conta1.extrato()

print()

conta1.saca(20.0)
conta1.extrato()

print()

conta1.historico.imprime()
novo_saque = -200.0
conta1.saldo = novo_saque
conta1.extrato()'''

'''print(type(conta))
print(conta.numero)
print(conta.titular)
conta.extrato()'''

'''cride = Pessoa(46)
cride._Pessoa_idade
print(dir(cride))
cride._idade = 30
print(cride._idade)
print(dir(cride))'''