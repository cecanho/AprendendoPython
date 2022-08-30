# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 004
# Data: 29-08-2022
# Objetivo: Operadores Aritméticos

# Operadores Aritméticos:
# +  Adição
# -  Subtração
# *  Multiplicação
# /  Divisão
# ** Potenciação

# Operador de adição
var_inteira = 1 + 1
print('Soma: 1 + 1')
print(var_inteira)

# Operador de subtração
var_inteira = 100 - 50
print('\nSutração: 100 - 50')
print(var_inteira)

# Operador de multiplicação
x = 9
y = 7
print('\nMultiplicação: x * y \nx = 9\ny = 7')
print(x * y)

# Operador de divisão
x = 1
y = 3
print('\nDivisão: x / y \nx = 1\ny = 3')
z = x / y
print(z)

# Operador de potenciação
x = 25
y = 2
print('\nPotenciação: x ** 2 \nx = 25')
z = x ** y
print(z)

# Divisão inteira
x = 25
y = 3
print('\nDivisão inteira: x // y \nx = 25\ny = 3')
z = x // y
print(z)

# Resto da divisão - exemplo para saber se um número é par divide este por 2,
# se o resto da divisão igual a 0 então o número é par
x = 24
y = 2
print('\nResto da divisão: x % y \nx = 24\ny = 2')
z = x % y
print(z)

# Concatenar Strings / Palavras / letras / símbolos / números
str1 = 'Olá '
str2 = 'Mundo'
str3 = ' Python'
str4 = '!'
print('\nConcatenação de strings')
print(str1 + str2 + str3 + str4)

# Operadores / Funções para strings
# Multiplicar string
print('\nMultiplicar String')
print(str3 * 3)

# Todas em Maiúsculo
print('\nTodas em Maiúsculo:')
print(str3.upper())

# Todas em Minúsculo
print('\nTodas em Minúsculo:')
print(str3.lower())

# Primeira letra em Maiúsculo
print('\nPrimeira letra em Maiúsculo:')
str5 = 'cristiano'
print(str5.capitalize())