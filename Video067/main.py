from funcionarios import Funcionarios
from funcionario import Funcionario
import csv

arquivo = open('funcionarios.txt', 'r')
leitor = csv.reader(arquivo)

funcionarios = Funcionarios()

for linha in leitor:
    funcionario = Funcionario(linha[0], linha[1], float(linha[2]))
    funcionarios.append(funcionario)

arquivo.close()

print(funcionarios.__len__())
print(funcionarios)

print(f"SALÁRIO\t+ BONIFICAÇÃO")
for f in funcionarios:
    print(f"{f.salario}\t+ {f.get_bonificacao()}")
