# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 008
# Data: 23-09-2022
# Objetivo: Resposta do exercício

# Exercício Exemplo
# Faça um programa em Python que dados três valores, a, b, c,
# são os comprimentos dos lados de um triângulo.
# Caso formem um triângulo o programa deve informar se formam qual tipo:
# equilátero,
# isóceles
# ou escaleno.
# Caso contrário informe que Não Formam Um Triângulo.

print('Informe três medidas positivas dos lados do triângulo')
a = int(input('Informe o lado A: \n'))
b = int(input('Informe o lado B: \n'))
c = int(input('Informe o lado C: \n'))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('As medidas dos lados informados formam um triângulo do tipo: ')
    if (a == b) and (a == c):
        print('EQUILÁTERO')
    elif (a == b) or (b == c) or (a == c):
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('As medidas dos lados informados não formam um triângulo!')