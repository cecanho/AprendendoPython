# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 021
# Data: 04-12-2022
# Objetivo: Funções - Exercícios página 74

# 1. Defina uma função chamada velocidade_media() em um script chamado funcoes.py que recebe
# dois parâmetros: a distância percorrida (em metros) e o tempo (em segundos) gasto.

# 2. Agora vamos inserir as instruções, ou seja, o que a função deve fazer. Vamos inserir os comandos
# para calcular a velocidade média e guardar o resultado em uma variável velocidade :

# 3. Vamos fazer a função imprimir o valor da velocidade média calculada:

# 4. Teste o seu código chamando a função para os valores abaixo e compare os resultados com seus
# colegas:
# distância: 100, tempo = 20
# distância: 150, tempo = 22
# distância: 200, tempo = 30
# distância: 50, tempo = 3

# 5. Modifique a função velocidade_media() de modo que ela retorne o resultado calculado.

# 6. Defina uma função soma() que recebe dois números como parâmetros e calcula a soma entre eles.

# 7. Defina uma função subtracao() que recebe dois números como parâmetros e calcula a diferença
# entre eles.

# 8. Agora faça uma função calculadora() que recebe dois números como parâmetros e retorna o
# resultado da soma e da subtração entre eles.

# 9. Modifique a função calculadora() do exercício anterior e faça ela retornar também o resultado da
# multiplicação e divisão dos parâmetros.

# 10. Chame a função calculadora() com alguns valores.

# 11. (opcional) Defina uma função divisao() que recebe dois números como parâmetros, calcula e
# retorna o resultado da divisão do primeiro pelo segundo. Modifique a função velocidade_media()
# utilizando a função divisao() para calcular a velocidade. Teste o seu código chamando a função
# velocidade_media() com o valores abaixo:
# a. distância: 100, tempo = 20
# b. distância: -20, tempo = 10
# c. distância: 150, tempo = 0

import funcoes

print('Distância: 100 \ttempo = 20 \tresultado = {} m/s'.format(funcoes.velocidade_media(100, 20)))
print('Distância: 150 \ttempo = 22 \tresultado = {} m/s'.format(funcoes.velocidade_media(150, 22)))
print('Distância: 200 \ttempo = 30 \tresultado = {} m/s'.format(funcoes.velocidade_media(200, 30)))
print('Distância: 50 \ttempo = 3 \tresultado = {} m/s'.format(funcoes.velocidade_media(50, 3)))

print('Somando entrada 1: 50 \t entrada 2: 3 \tresultado = {}'.format(funcoes.soma(50, 3)))
print('Subtraindo entrada 1: 50 \t entrada 2: 3 \tresultado = {}'.format(funcoes.subtracao(50, 3)))

print('\n')
funcoes.calculadora(10, 2)

print('\n')
print('Distância: 100 \ttempo = 20 \tresultado = {} m/s'.format(funcoes.velocidade_media(100, 20)))
print('Distância: -20 \ttempo = 10 \tresultado = {} m/s'.format(funcoes.velocidade_media(-20, 10)))
print('Distância: 150 \ttempo = 0 \tresultado = {} m/s'.format(funcoes.velocidade_media(150, 0)))