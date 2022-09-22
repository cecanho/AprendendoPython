# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 007
# Data: 21-09-2022
# Objetivo: IF, ELSE e ELIF

# Comando IF
# JOGO DE ADIVINHAÇÃO
numInt = 335
chute = int(input('Entre com um número entre 0 e 1000\n'))
print('Você digitou: ', chute)
# if numInt == chute:
#     print('Você acertou!!!')

# Comando IF ELSE
# if numInt == chute:
#     print('Você acertou!!!')
# else:
#     print('Você errou!')

# Comando ELIF
if numInt == chute:
    print('Você acertou!!!')
elif numInt < chute:
    print('Você errou! Chutou um número maior...')
elif numInt > chute:
    print('Você errou! Chutou um número menor...')

# Exercício Exemplo
# Faça um programa em Python que dados três valores, a, b, c, são os comprimentos dos lados de
# um triângulo. Caso formem um triângulo o programa deve informar se formam qual tipo: equilátero, isóceles
# ou escaleno. Caso contrário informe que Não Formam Um Triângulo.