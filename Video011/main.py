# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 011
# Data: 21-10-2022
# Objetivo: Exemplo de simulação do Do While

flag = 1
contador = 1

while (flag != 0):
    print('Executando ', contador,' vez(es).')
    contador = contador + 1
    if (contador > 3):
        flag = 0