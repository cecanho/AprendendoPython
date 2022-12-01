# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 019
# Data: 26-11-2022
# Objetivo: Funções - parâmetros default

def velocidade(espaco, tempo=None):
    if (tempo == None):
        print('Velocidade igual a {} m/s'.format(espaco / 20))
    else:
        print('Velocidade igual a {} m/s'.format(espaco / tempo))

velocidade(100, 30)
velocidade(100)