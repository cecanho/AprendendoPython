# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 010
# Data: 03-10-2022
# Objetivo: Comando Para/For

numero_secreto = 5
print('Jogo da adivinhação!\n')

for tentativa in range(1, 4):

    print('Tentativa {} de 3\n'.format(tentativa))
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

print('Fim de jogo!')
