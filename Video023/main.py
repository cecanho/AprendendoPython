# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 022
# Data: 15-12-2022
# Objetivo: Número arbitrário de parâmetros (*args)

'''

*args       - *
**kwargs    - **

'''

def argumentos(arg, *args):
    print(f"Primeiro argumento da função normal é {arg}")
    for arg in args:
        print(f"Parâmetro externo: {arg}")

argumentos('Python', 'é', 'muito', 'legal')

lista = ["é", "muito", "legal"]

argumentos('Python', *lista)

# **kwargs

def kargumentos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}")
        # print('{0}={1}'.format(key,value))

kargumentos(nome='caelum')

# passando um dicionário
dicionario = {'nome' : 'Cristiano', 'idade' : 46}
kargumentos(**dicionario)