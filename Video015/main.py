# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 015
# Data: 13-11-2022
# Objetivo: Conjuntos

# Conjunto de palavras criado com chaves não ordenado e que não permite duplicatas
frutas = {'laranja', 'banana', 'uva', 'pera', 'maçã', 'mamão', 'amora', 'uva', 'pera'}
print(frutas)
print(type(frutas))

# Conjunto criado com a função set()
a = set('abacate')
b = set('abacaxi')
print(type(a))
print(a)
print(type(b))
print(b)
# a diferença do conjunto a para o b
print(a - b)
# a diferença do conjunto b para a
print(b - a)
# a união dos conjuntos
print(a | b)
# a interseção de a e b
print(a & b)
# a diferença simétrica entre a e b
print(a ^ b)

# a diferença de criar conjunto vazio com {} e com a função set()
c = {}
d = set()

print(type(c))
print(c)
print(type(d))
print(d)
