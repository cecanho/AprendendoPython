'''
Autor: Cristiano José Cecanho
Aprendendo Python: Vídeo 024
Data: 20-12-2022
Objetivo: Exercícios pag. 70 ~ 77
'''

'''
1. Crie um arquivo com uma função chamada teste_args_kwargs() que recebe três argumentos e
imprime cada um deles:
'''

'''
def teste_args_kwargs(arg1, arg2, arg3):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"arg3: {arg3}")
'''

'''
def teste_args_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        '''

def teste_args_kwargs(*args, **kwargs):
    contador = 1
    if(len(args) != 0):
       for arg in args:
           print(f"arg{contador}: {arg}")
           contador += 1
    else:
        for key, value in kwargs.items():
            print(f"{key}: {value}")

'''
2. Agora vamos chamar a função utilizando o *args:
arg1: um
arg2: 2
arg3: 3
'''

teste_args_kwargs(1)

print()
args = ('um', 2 , 3)
# print(type(args))
teste_args_kwargs(*args)

'''
3. Teste a mesma função usando o **kwargs. Para isso, crie um dicionário com três argumentos:
'''
# kwargs = {'arg3' : 3, 'arg2' : 'dois', 'arg1' : 'um'}

'''
4. Adicionando um quarto elemento chave valor ao dicionário
'''
kwargs = {'arg4': 4, 'arg3' : 3, 'arg2' : 'dois', 'arg1' : 'um'}
# print(type(kwargs))
print()
teste_args_kwargs(**kwargs)