def cria_conta(numero, titular, saldo, limite):
    '''
     cria_conta(numero, titular, saldo, limite)
     conta = {}
     conta = teste_conta.cria_conta('###-#', 'Nome', ####.#, ####.#)
     Retorna uma conta preenchida com os dados do parâmetro
    '''
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    '''
     deposita(conta,valor)
     teste_conta.deposita(conta, ####.#)
     Retorna um deposito na conta informada com o valor informado no parâmetro
    '''
    conta['saldo'] += valor

def saca(conta, valor):
    '''
     sacaa(conta,valor)
     teste_conta.saca(conta, ####.#)
     Retorna um saca na conta informada com o valor informado no parâmetro
    '''
    conta['saldo'] -= valor

def extrato(conta):
    '''
     extrato(conta)
     teste_conta.extrato(conta)
     Retorna informações da conta como número, titular, saldo, limite e saldo + limite
    '''
    print(f"Num.: {conta['numero']}\n"
          f"Titular: {conta['titular']}\n"
          f"Saldo(a): {conta['saldo']}\n"
          f"Limite(b): {conta['limite']}\n"
          f"Total(a + b): {conta['limite'] + conta['saldo']}\n")

'''
def help(valor):
    if (valor == ''):
        print(f"c - cria_conta(numero, titular, saldo, limite): cria uma conta\n"
              f"d - deposita(conta, valor): faz um depósito\n"
              f"s - saca(conta, valor): faz um saque\n"
              f"e - extrato(conta): exibe dados da conta\n")
    elif(valor == 'c'):
        print(f"cria_conta(numero, titular, saldo, limite)\n"
              f"conta = teste_conta.cria_conta('###-#', 'Nome', ####.#, ####.#\n"
              f"Retorna uma conta preenchida com os dados do parâmetro\n")
    elif(valor == 'd'):
        print(f"deposita(conta,valor)\n"
              f"teste_conta.deposita(conta, ####.#)\n"
              f"Retorna um deposito na conta informada com o valor informado no parâmetro\n")
    elif (valor == 's'):
        print(f"sacaa(conta,valor)\n"
              f"teste_conta.saca(conta, ####.#)\n"
              f"Retorna um saque na conta informada com o valor informado no parâmetro\n")
    elif (valor == 'e'):
        print(f"extrato(conta)\n"
              f"teste_conta.extrato(conta)\n"
              f"Retorna informações da conta como número, titular, saldo, limite e saldo + limite\n")
    else:
        help('')
        '''