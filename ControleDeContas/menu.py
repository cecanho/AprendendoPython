from Contas import Contas
from ListaContas import ListaContas
import csv

def menu(op, salario):

    lc = ListaContas()
    total = 0.0

    while (op != '7'):
        print(f"1 - Abrir arquivo")
        print(f"2 - Salvar em arquivo")
        print(f"3 - Adicionar conta")
        print(f"4 - Alterar valor de conta por ID")
        print(f"5 - Excluir conta por ID")
        print(f"6 - Imprimir contas")
        print(f"7 - Sair")
        op = input(f"Escolha uma das opções:\t")

        if op == '1':
            print(f"Abrir arquivo")
            arquivo = open('contas.csv', 'r')
            leitor = csv.reader(arquivo)

            for l in leitor:
                conta = Contas(l[0], float(l[1]))
                total += conta.valor
                lc.insert(conta)
            arquivo.close()
            print(f"Total de contas cadastradas: {lc.__len__()}")
            print(f"Salário: {salario}")
            print(f"Valor Total das contas cadastradas: {total}")

        elif op == '2':
            print(f"Salvar em arquivo")
            txt = ''
            arquivo = open('contas.csv', 'w')
            for l in lc:
                txt = txt + l.nome + ',' + str(l.valor) + '\n'
            arquivo.write(txt)
            arquivo.close()

        elif op == '3':
            print(f"Adicionar conta")
            nome = input(f"Informe o nome da conta: ")
            valor = float(input(f"Informe o valor da conta R$ "))
            conta = Contas(nome, valor)
            lc.insert(conta)
            print(f"Conta adicionada com sucesso, total de contas = {lc.__len__()}")
            print(f"Salário: {salario}")
            total += conta.valor
            print(f"Valor Total das contas cadastradas: {total}")

        elif op == '4':
            print(f"Alterar valor de conta por ID")
            id = int(input(f"Informe o ID da conta: "))
            valor = float(input(f"Informe novo valor da conta R$ "))
            lc.__setitem__(id, valor)
            print(f"A conta de ID {id} foi alterada com sucesso!")

        elif op == '5':
            print(f"Excluir conta por ID")
            print(f"ID\tCONTA\tVALOR")
            id = 0
            for l in lc:
                print(f"{id}\t{l.nome}\t{l.valor}")
                id += 1
            escolha = int(input(f"Qual conta excluir? ID = "))
            lc.__delitem__(escolha)
            print(f"Conta excluída com sucesso!")

        elif op == '6':
            print(f"ID\tCONTA\tVALOR")
            total = 0.0
            id = 0
            for l in lc:
                print(f"{id}\t{l.nome}\t{l.valor}")
                total += l.valor
                id += 1
            print(f"Total de contas cadastradas: {lc.__len__()}")
            print(f"Salário: {salario}")
            print(f"Valor Total das contas cadastradas: {total}")

        elif op == '7':
            print(f"Bye!")