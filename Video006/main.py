# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 006
# Data: 12-09-2022
# Objetivo: Constantes embutidas em Python

# Constantes booleanas True e False

print('Comparando valores int com str 1 == \'1\'')
print(1 == '1')

# Comparação de inteiros
print(1 == 1)

# Impressão de valor booleano verdadeiro
print(bool(1))

# Impressão de valor falso
print(bool(''))

# Abstensão de um valor, semelhante a NULL
print(bool(None))
print(bool(0))

# Operadores lógicos de comparação

#   Operador            Descrição
#    a == b          a igual a b
#    a != b          a diferente de b
#    a < b           a menor do que b
#    a > b           a maior do que b
#    a <= b          a menor ou igual a b
#    a >= b          a maior ou igual a b

# Operadores de comparação booleanos

#   Operador            Descrição
#   a is b          True se a e b são idênticos
#   a is not b      True se a e b não são idênticos
#   a in b          True se a é membro de b
#   a not in b      True se a não é membro de b

# Teste de operadores de comparação
x = [1, 2, 3]
y = [1, 2, 3]

print('Comparação de igualdade x == y')
print(x == y)
print('Comparação se são iguais x is y')
print(x is y)
print('Comparação se um conjunto está em outro x in y')
print(x in y)
print('Comparação se um número pertence a conjunto 1 in x')
print(1 in x)

