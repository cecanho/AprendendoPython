# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 011
# Data: 25-10-2022
# Objetivo: Estrutura de dados: lista


print('*****************JOGO DA ADVINHAÇÃO*****************')

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
palavra_secreta = palavra_secreta.lower()
acertou = False
enforcou = False

while(not acertou and not enforcou):
    print('Jogando...')

    errou = False

    while(not acertou and not errou):
        chute = input('Qual a letra?')
        chute = chute.lower()
        posicao = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print('Encontrei a letra {} na posição {}'.format(letra, posicao))
                letras_acertadas[posicao] = letra
            posicao = posicao + 1
        print(letras_acertadas)

print('Fim de Jogo')