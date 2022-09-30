# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 009
# Data: 29-09-2022
# Objetivo: Comando Enquanto/while

tentativas = 3
incremento = 0
numero_secreto = 5
print('Jogo da adivinhação!\n')

while(tentativas != incremento):

    print('Tentativa {} de 3\n'.format(incremento + 1))
    numero_sugerido = int(input('Que número pensei?\nDigite um valor entre 1 e 10: '))

    igual = numero_secreto == numero_sugerido
    maior = numero_sugerido > numero_secreto
    menor = numero_sugerido < numero_secreto

    if(igual):
        print('Danado, você acertou!!!')
        break
    elif(maior):
        print('Oops, número digitado é maior que número secreto...')
    elif(menor):
        print('Oops, número digitado é menor que número secreto...')

    incremento = incremento + 1

print('Fim de jogo!')
