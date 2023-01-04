'''
Aprendendo Python: Vídeo 029
Autor: Cristiano José Cecanho
Data: 04-01-2023
Tema: Introdução a Orientação a Objetos (OO)
'''

# Funcionalidades de uma entidade conta bancária com dicionário de dados
def criar_conta(numero, titular, saldo):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': 1000.0}
    return conta

# Funcionalidade depositar
def depositar(conta, valor):
    conta['saldo'] += valor

# Funcionalidade sacar
def sacar(conta, valor):
    conta['saldo'] -= valor

# Funcionalidade extrato
def extrato(conta):
    print(f"Num: {conta['numero']}"
          f"\nTitular: {conta['titular']}"
          f"\nSaldo (a): {conta['saldo']}"
          f"\nLimite (b): {conta['limite']}"
          f"\nLim. Total(a+b): {conta['saldo'] + conta['limite']}")

# Criando uma conta
conta = criar_conta('123-4', 'Pingo', 120.0)

# Deposito em uma conta
depositar(conta, 150.0)

# Saque de uma conta
sacar(conta, 13.0)

# Extrato de uma conta
extrato(conta)

# Experimente descomentar as linhas abaixo
conta2 = criar_conta('123-5', 'Cristiano', '10.0')
#depositar(conta2, 150.0)
#sacar(conta2, 13.0)
#extrato(conta2)