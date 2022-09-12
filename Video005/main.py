# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 004
# Data: 29-08-2022
# Objetivo: Entrada do usuário e o cálculo da área de um triângulo

# Entrada do usuário
#entrada = input()

#print(entrada)

# Recebendo e imprimindo um valor
print('Digite um nome: ')
nome = input()
print('O nome digitado foi: ' + nome)
print('Qual a sua idade?')
idade = input()
# print concatenado
print('O nome digitado foi ' + nome + ' e tem idade igual a ' + idade)
# comando format()
print('O nome digitado foi {} e tem idade igual a {}'.format(nome, idade))

# Cálculo da área de um triângulo: base * altura / 2
print('##### Cálculo da área de um triângulo #####\n')
print('Digite a medida da base do triângulo:')
baset = input()
print(type(baset))
print('Digite a medida da altura do triângulo:')
alturat = input()
print(type(alturat))
areat = int(baset) * int(alturat) / 2
print(type(areat))
print('A área do triângulo de base {} e de altura {} é igual a {}'.format(baset, alturat, areat))