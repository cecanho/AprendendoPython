# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 018
# Data: 25-11-2022
# Objetivo: Funções

def boas_vindas():
    print('Vídeo 018 - Aprendendo funções em Python')

def mensagem_saida():
    print('Bye!')

# criar f(espaço, tempo) = espaço/tempo

# velocidade(espaco/tempo) = espaco/tempo

# velocidade(100, 20) = 100/20 = 5 m/s

def velocidade(espaco, tempo):
    v = espaco / tempo
    print('Velocidade: {} m/s'.format(v))

listas = {}
lista = 1

boas_vindas()

print(type(listas))
print(type(lista))

velocidade(100, 20)

mensagem_saida()

