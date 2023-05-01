from conta import Conta
from contaCorrente import CC
from excecoes import SaldoInsuficienteError

class CaixaEletronico(Conta):
    pass

if __name__ == '__main__':
    cc = CC('123-4', 'João', 1000.0, 1000.0)

    print(f"CAIXA ELETRÔNICO\n"
          f"BEM VINDO\n"
          f"----------------\n"
          f"1 - Depósito\n"
          f"2 - Saque\n"
          f"3 - Saldo\n"
          f"0 - Sair\n"
          f"Escolha um número 1 - 2 - 3")

    opcao = int(input())

    if (opcao == 1):
        valor = float(input(f"Qual valor a depositar?"))
        try:
            cc.deposita(valor)
            print(f"Deposito de {valor} realizado com sucesso")
        except ValueError:
            print(f"O valor a ser depositado deve ser positivo")
        except SaldoInsuficienteError:
            print('Você não possui saldo suficiente para concluir esta operação.')
    elif (opcao == 2):
        valor = float(input(f"Qual valor a sacar?"))
        try:
            cc.saca(valor)
            print(f"Saque de {valor} realizado com sucesso")
        except ValueError:
            print(f"O valor a ser sacado deve ser positivo")
        except SaldoInsuficienteError:
            print('Você não possui saldo suficiente para concluir esta operação.')
    elif (opcao == 3):
        print(f"Saldo = {cc.saldo}")