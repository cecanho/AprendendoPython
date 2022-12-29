'''
Aprendendo Python: Vídeo 027
Autor: Cristiano José Cecanho
Data da criação: 29/12/2022
Tema: Arquivos
Fonte: https://www.caelum.com.br/apostila/apostila-python-orientacao-a-objetos.pdf
'''

import random

# Arquivos

'''
Abrir arquivo - open(parametro1, parametro2)
- parametro1: 'nome-do-arquivo.ext'
- parametro2: 'modo-de-leitura'
-- modo de leitura: w - escrita (write), r - leitura (read)
'''

# Abertura do Arquivo em modo escrita
# arquivo = open('palavras.mtxt', 'w')

# Write
'''
arquivo.write('Adriano\n')
arquivo.write('Anabele\n')
'''

# Abertura do Arquivo em modo adição
# arquivo = open('palavras.mtxt', 'a')

# Append
'''
arquivo.write('\nValdir')
arquivo.write('\nRoberta')
'''

# Read
arquivo = open('palavras.mtxt', 'r')
# não suportado pois está em modo leitura
# arquivo.write('\noi')

# leitura vazia do arquivo
# arquivo.read()

# lista de nomes
nomes = []

# lendo o conteúdo do arquivo
for linha in arquivo:
    linha = linha.strip()
    nomes.append(linha)
    print(linha)

# Fechando o arquivo
arquivo.close()

numero = random.randrange(0, len(nomes))
nomeSorteado = nomes[numero].upper()

print(f"O nome sorteado foi {nomeSorteado} e está na posição {numero}")