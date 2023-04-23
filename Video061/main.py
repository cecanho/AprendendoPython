# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 061
# Data: 23-04-2023
# Objetivo: Tratando exceções

n1 = 10
n2 = 0

'''try:
    resultado = n1 / n2
    print(f"Resulado {n1} / {n2} = {resultado}")
except ZeroDivisionError:
    print(f"Divisão por ZERO")'''

'''try:
    arquivo = open('palavras.txt', 'r')
except IOError:
    print('não foi possível abrir o arquivo')
else:
    print('o arquivo tem {} palavras'.format(len(arquivo.readlines())))
    arquivo.close()'''
try:
    raise NameError('oi')
except:
    print(f"Lançou uma exceção")
    raise