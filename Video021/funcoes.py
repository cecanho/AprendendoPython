def velocidade_media(distancia, tempo):
    return divisao(distancia, tempo)

def soma(num_1, num_2):
    return num_1 + num_2

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(num_1, num_2):
    return num_1 * num_2

def divisao(num_1, num_2):
    if (num_2 == 0):
        return 0
    else:
        return num_1 / num_2

def calculadora(num_1, num_2):
    print('A soma de {} com {} é igual a: {}'.format(num_1, num_2, soma(num_1, num_2)))
    print('A subtração de {} com {} é igual a: {}'.format(num_1, num_2, subtracao(num_1, num_2)))
    print('A multiplicação de {} com {} é igual a: {}'.format(num_1, num_2, multiplicacao(num_1, num_2)))
    print('A divisão de {} com {} é igual a: {}'.format(num_1, num_2, divisao(num_1, num_2)))