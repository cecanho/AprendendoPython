import csv

try:
    arquivo = open('funcionarios.csv', 'r')
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
except:
    print(f"Arquivo não encontrado!")
finally:
    arquivo.close()