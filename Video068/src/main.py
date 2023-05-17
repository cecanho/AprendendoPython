# 1. Vá na pasta no curso e copie o arquivo contas.txt na pasta src do projeto banco que contém
# vários dados de contas correntes de clientes do banco.
# 2. Crie um arquivo chamado contas.py na pasta src do projeto banco . Crie uma classe chamada
# Contas que herde da classe abstrata MutableSequence
# 3. Vamos criar um atributo na classe chamado _dados do tipo list para armazenar nossas contas
# 4. Tente instanciar um objeto de tipo Contas
# 5. Implemente os métodos exigidos pela interface MutableSequence na classe Contas
# 6. Nossa sequência só deve permitir adicionar elementos que sejam do tipo Conta . Vamos acrescentar
# essa validação nos métodos __setitem__ e insert . Caso o valor não seja uma Conta , vamos
# lançar um TypeError com as devidas mensagens de erro
# 7. Vamos iniciar a leitura dos dados do arquivo para armazenar em nosso objeto contas
# 8. Vamos criar uma laço for para ler cada linha do arquivo e construir um objeto do tipo
# ContaCorrente
# 9. Queremos inserir cada conta criada em nossa sequência mutável contas . Vamos pedir para que o
# programa acrescente cada conta criada em contas
# 10. Nossa classe Contas implementa MutableSequence . Isso quer dizer que ela é iterável já que
# MutableSequence implementa o protocolo __iter__ através do método __getitem__ . Vamos
# iterar através de uma laço for nosso objeto contas e pedir para imprimir o saldo e o valor do
# imposto de cada uma delas
# 11. (Opcional) Modifique o código do exercício anterior de modo que imprima o valor do saldo
# atualizado das contas.
# 12. Opcional) Faça o mesmo com as contas poupanças. Crie um arquivo com extensão .csv com
# algumas contas poupanças, faça a leitura, construa os objetos e acrescente em uma estrutura de
# dados do tipo MutableSequence .
# 13. (Desafio Opcional) Refaça o exercício utilizando MutableMapping ao invés de
# MutableSequence .

# c = Conta('123-4', 'José', 5000.0, 0)

from contas import Contas
from contaCorrente import CC
from contaPoupanca import CP

contas = Contas()

import csv
arquivo = open('contas.txt', 'r')
leitor = csv.reader(arquivo)

for linha in leitor:
    conta = CC(linha[0], linha[1], linha[2], float(linha[3]))
    contas.append(conta)

arquivo.close()

print(f"Total de contas (CC): {contas.__len__()}")

print(f"SALDO \t- IMPOSTO")

for c in contas:
    print(f"{c.saldo - c.get_valor_imposto()} \t- {c.get_valor_imposto()}")

contasPoupancas = Contas()

arquivo2 = open('contaPoupanca.csv', 'r')
leitor2 = csv.reader(arquivo2)

for linha2 in leitor2:
    contasPoupanca = CP(linha2[0], linha2[1], linha2[2], float(linha2[3]))
    contasPoupancas.append(contasPoupanca)

arquivo2.close()
print()
print(f"Total de contas (CP): {contasPoupancas.__len__()}")

print(f"SALDO \t- RENDIMENTO")

for cp in contasPoupancas:
    print(f"{cp.saldo} \t- {cp.atualiza(0.15)}")