# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 025
# Data: 23-12-2022
# Objetivo: jogo da forca

import random
import os

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_abertura():
    # no prompt para  Windows
    os.system('cls') or None
    # no terminal do Linux
    # os.system('clear') or None
    print('****************************************************')
    print('*******************JOGO DA FORCA********************')
    print('****************************************************')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return  chute

def imprimir_mensagem_vencedor():
    print('Você Ganhou!!!')

def imprimir_mensagem_perdedor(palavra_secreta):
    print('Você Perdeu!!!')
    print('A palavra secreta era: {}'.format(palavra_secreta))