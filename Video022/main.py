'''
Autor: Cristiano Jose Cecanho
Aprendendo Python: Video 022
Data: 12/12/2022
Objetivo: Respondendo comentarios e diferença entre Python 2 e 3

Font: https://python.org.br/qual-python

Criado 1989
Python 2
- Descontinuado em 2020
- Sistemas legados

Python 3
- E aadequaçao para acertar a compatibilidade com novos dispositivos
- E o a versao que continua recebendo atualizaçoes
'''

print('Ola mundo')
# Descontinuado da versao 2 para a 3
# print 'Ola Mundo'

# Leitura de multiplas variaveis
nome, idade, altura = 'Cristiano', 45, 1.69

print(type(nome))
print(nome)
print(type(idade))
print(idade)
print(type(altura))
print(altura)

print('Nome:', nome, 'Idade:', idade, 'Altura:', altura)
print('Nome: ' + nome + ' Idade: ' + str(idade) + ' Altura: ' + str(altura))

# fonte: https://pythonacademy.com.br/blog/f-strings-no-python
# f-strings
nome = 'Cristiano Jose Cecanho'

# No formato com o uso de format()
print('O nome e {}'.format(nome))

# No formato f-strings
print(f"O nome e {nome}")

curso = 'python'
print(f"Aprendendo {curso.upper() + '!' * 2}")