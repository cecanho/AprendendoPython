class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total

if __name__ == '__main__':
    from contaCorrente import CC
    from seguroDeVida import SeguroDeVida
    from TributavelMixIn import TributavelMixIn

    cc1 = CC('123-4', 'PF', 'José', 1000.0)
    cc2 = CC('124-4', 'PF', 'Manuel', 1000.0)
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)