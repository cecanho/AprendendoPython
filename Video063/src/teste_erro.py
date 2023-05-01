from contaCorrente import CC

def metodo1():
    print('Início do método 1')
    metodo2()
    print('Fim do método 1')

def metodo2():
    cc = CC('123-4', 'PF', 'José', 1000.0)
    print('início do metodo 2')
    for i in range(1, 15):
        cc.deposita(i + 1000)
        print(cc.saldo)
        if (i == 5):
            cc = None
    print('fim do metodo 2')

if __name__ == '__main__':
    print('início do main')
    try:
        metodo1()
    except:
        print('erro')
    print('fim do main')