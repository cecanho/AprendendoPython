# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 020
# Data: 26-11-2022
# Objetivo: Funções - retorno de valor

def velocidade(espaco, tempo=None):
    if (tempo == None):
        return espaco / 20
    else:
        return espaco / tempo

def calculadora(x, y):
    return {'Soma': x + y, 'Subtração': x - y}

print(calculadora(5, 3))

resultados = calculadora(6, 7)

print(type(resultados))

for key in resultados:
    print('{}: {}'.format(key, resultados[key]))

print('A velocidade é igual a {} m/s'.format(velocidade(100, 30)))
print('A velocidade é igual a {} m/s'.format(velocidade(100)))

print('Entre com o espaço em Km')
espaco = int(input())
tempo = int(input('Entre com a quantidade de horas'))
print('A velocidade é igual a {} km/h'.format(velocidade(espaco, tempo)))


espaco = int(input('Entre com o espaço em Km'))
print('A velocidade é igual a {} km/h'.format(velocidade(espaco)))