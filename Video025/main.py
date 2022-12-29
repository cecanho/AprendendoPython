# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 025
# Data: 23-12-2022
# Objetivo: Resolução do exercício jogo da forca e da adivinhação com import

'''
1. Vamos começar definindo uma função jogar que conterá toda lógica do jogo da forca. Abra o
arquivo forca.py e coloque o código do jogo em uma função jogar()
Em seguida, chame a função jogar() logo abaixo da definição da função no arquivo forca.py:

2. Faça o mesmo com o jogo da adivinhação e execute o jogo:
'''

import forca
import adivinhacao

print('*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print('1. Adivinhação')
print('2. Forca')
escolha = int(input("Qual jogo quer jogar? Digite o número: "))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()
else:
    print('Opção inválida! Bye!!')