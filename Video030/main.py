# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 030
# Data: 06-01-2023
# Objetivo: exercícios de OO (8.2)

'''
1. Crie uma pasta chamada oo em sua workspace e crie um arquivo chamado teste_conta.py

2. Crie a função chamada cria_conta() , que recebe como argumento numero , titular , saldo e
limite :
def cria_conta(numero, titular, saldo, limite):

3. Dentro de cria_conta() , crie uma variável do tipo dicionário chamada conta com as chaves
recebendo os valores dos parâmetros ( numero , titular , saldo e limite ), e ao final, retorne a
conta :

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

4. Crie uma função chamada deposita() no mesmo arquivo teste_conta.py que recebe como
argumento uma conta e um valor . Dentro da função, adicione o valor ao saldo da conta:
def deposita(conta, valor):
conta['saldo'] += valor

5. Crie outra função chamada saca() que recebe como argumento uma conta e um valor . Dentro
da função, subtraia o valor do saldo da conta:
def saca(conta, valor):
    conta['saldo'] -= valor

6. E por fim, crie uma função chamada extrato() , que recebe como argumento uma conta e
imprime o numero e o saldo :
def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

7. Navegue até a pasta oo , digite os comandos no arquivo teste_conta.py e teste as funcionalidades:
conta = cria_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)

#numero: '123-7'
#saldo: 550.0
saca(conta, 20.0)
extrato(conta)

#numero: '123-7'
#saldo 530.0

8. (Opcional) Acrescente uma documentação para o seu módulo teste_conta.py e utilize a função
help() para testá-la.

'''

from oo import teste_conta

conta = {}

# Exercício 7

conta = teste_conta.cria_conta('123-7', 'João', 500.0, 1000.0)
teste_conta.deposita(conta, 50.0)
teste_conta.extrato(conta)

# Num.: '123-7'
# Titular: 'João'
# Saldo: 550.0
# Limite(a): 1000.0
# Total(a + b): 1550.0

teste_conta.saca(conta, 20.0)
teste_conta.extrato(conta)

# Num.: '123-7'
# Titular: 'João'
# Saldo: 530.0
# Limite(a): 1000.0
# Total(a + b): 1530.0

'''
teste_conta.help('')
teste_conta.help('c')
teste_conta.help('d')
teste_conta.help('s')
teste_conta.help('e')
teste_conta.help('t')
'''

help(teste_conta.cria_conta)