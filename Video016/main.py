# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 016
# Data: 13-11-2022
# Objetivo: Dicionários

pessoa = {'nome': 'Cristiano', 'idade': '46', 'cidade': 'Rio Claro'}
print(type(pessoa))
print(pessoa)

# Forma errada
# print(pessoa[0])

# Forma correta
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])

# Adicionando mais uma chave
pessoa['pais'] = 'Brasil'

print(pessoa['pais'])

print(pessoa.keys())
print(pessoa.values())

# Tuples com dict
# dic = {[1, 2, 3]: 'valor'}
dic = {(1, 2, 3): 'valor'}
print(dic)

# dict() é igual a função set()
dic2 = dict(um=1, dois=2, tres=3)
print(dic2)

# Diferença entre os dois
print(type(dic))
print(type(dic2))