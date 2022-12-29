# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 025
# Data: 23-12-2022
# Objetivo: jogo da adivinhação

import random
import os

def jogar():
    mensagem()
    numInt = int(random.randrange(0, 1000))
    chute = int(input('Entre com um número entre 0 e 1000\n'))
    print('Você digitou: ', chute)

    if numInt == chute:
        print('Você acertou!!!')
    elif numInt < chute:
        print('Você errou! Chutou um número maior...')
        print(f"O número  era: {numInt}")
    elif numInt > chute:
        print('Você errou! Chutou um número menor...')
        print(f"O número  era: {numInt}")

def mensagem():
    # No prompt do Windows
    os.system('cls') or None
    # No terminal do Linux
    # os.system('clear') or None
    print('****************************************************')
    print('****************JOGO DA ADIVINHAÇÃO*****************')
    print('****************************************************')