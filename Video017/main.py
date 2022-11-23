# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 017
# Data: 13-11-2022
# Objetivo: Exercício

# Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
# a) imprima o maior elemento
# b) imprima o menor elemento
# c) imprima os números pares
# d) imprima o número de ocorrências do primeiro elemento da lista
# e) imprima a média dos elementos
# f) imprima a soma dos elementos de valor negativo

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
listaPares = []
ocorrencias = 0
media = 0
somaNegativos = 0

# Resolução a), b), c), d), e)
print('Percorrendo a lista')
print('O maior elemento da lista é: ')
menor = maior = lista[0]


for indice in range(0, len(lista)):
    if (maior < lista[indice]):
        maior = lista[indice]
    if (menor > lista[indice]):
        menor = lista[indice]
    if (lista[indice]%2==0):
        listaPares.append(lista[indice])
    if (lista[0] == lista[indice]):
        ocorrencias += 1
    media += lista[indice]
    if (lista[indice] < 0):
        somaNegativos += lista[indice]
print(maior)

print('O menor elemento da lista é: ')
print(menor)
print('Os números pares da lista são: ')
print(listaPares)
print('A ocorrência do primero elemento {} é: '.format(lista[0]))
print(ocorrencias)
print('A média da lista é: ')
print(media/len(lista))
print('A soma dos negativos é igual a: ')
print(somaNegativos)
print('\n')

print('Utilizando as funções max e min')
print('O maior elemento da lista é: ')
print(max(lista))
print('O menor elemento da lista é: ')
print(min(lista))
print('A média da lista é: ')
print(sum(lista)/len(lista))