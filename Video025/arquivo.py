'''
Exercício referente as páginas 75-82
'''
def abrir():
    arquivo = open('palavras.txt', 'w')
    arquivo.write('banana\n')
    arquivo.write('melancia\n')
    arquivo.write('pera\n')
    arquivo.write('manga\n')
    arquivo.write('abacate\n')
    arquivo.close()