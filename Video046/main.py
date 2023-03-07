# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 047
# Data: 04-03-2023
# Objetivo: OO em Python - Reescrita e Métodos

from gerente import Gerente
from funcionario import Funcionario

funcionario = Funcionario('José',
                          'Avenida Ulisses Guimarães, n. 5, Vila Indaiá, Rio Claro - SP',
                          '122.122.123-12',
                          '19-1233-1234',
                          '19-12335-1234',
                          'ze_do@banco.com',
                          'Gerente',
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

print(gerente.nome)
print(gerente.funcao)
print(gerente.salario)
print(gerente.qtdFuncionarios)
if(gerente.autentica('cristiano','123456')):
    print(f"\nACESSO CONCEDIDO")
else:
    print(f"\nACESSO NEGADO")

print(gerente.get_bonificacao())

print(vars(gerente))
print(vars(funcionario))