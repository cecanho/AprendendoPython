# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 049
# Data: 11-03-2023
# Objetivo: OO em Python - Polimorfismo
from Cliente import Cliente
from gerente import Gerente
from funcionario import Funcionario
from ControleDeBonifcacoes import ControleDeBonificacoes

faxineiro = Funcionario('José',
                          'Avenida Ulisses Guimarães, n. 5, Vila Indaiá, Rio Claro - SP',
                          '122.122.123-12',
                          '19-1233-1234',
                          '19-12335-1234',
                          'ze_do@banco.com',
                          'Faxineiro',
                          2000.0
                          )

gerente = Gerente('Cristiano',
                 'Avenida Ulisses Guimarães, n. 1, Vila Indaiá, Rio Claro - SP',
                 '123.123.123-12',
                 '19-1234-1234',
                 '19-12345-1234',
                 'cristiano@banco.com',
                      'Gerente',
                      5000.0,
                  'cristiano',
                  '123456',
                  12)

cliente = Cliente('Manuel',
                          'Avenida Ulisses Guimarães, n. 109, Vila Indaiá, Rio Claro - SP',
                          '124.142.143-12',
                          '19-1233-1434',
                          '19-12335-1434',
                          'manuel@banco.com',
                          '111-1',
                          '001'
                          )

controle = ControleDeBonificacoes()
controle.registra(faxineiro)
controle.registra(gerente)
controle.registra(cliente)
print(f"Bonificação Faxineiro: {faxineiro.get_bonificacao()}")
print(f"Bonificação Gerente: {gerente.get_bonificacao()}")
print(f"Total: {controle.total_bonificacoes}")

'''print(gerente.nome)
print(gerente.funcao)
print(gerente.salario)
print(gerente.qtdFuncionarios)
if(gerente.autentica('cristiano','123456')):
    print(f"\nACESSO CONCEDIDO")
else:
    print(f"\nACESSO NEGADO")

print(gerente.get_bonificacao())

print(vars(gerente))
print(vars(funcionario))'''