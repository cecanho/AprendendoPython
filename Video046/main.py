# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 046
# Data: 26-02-2023
# Objetivo: OO em Python - Herança

from gerente import Gerente

pessoa1 = Gerente('Cristiano',
                 'Avenida Ulisses Guimarães, n. 1, Vila Indaiá, Rio Claro - SP',
                 '123.123.123-12',
                 '19-1234-1234',
                 '19-12345-1234',
                 'cristiano@banco.com',
                      'Gerente',
                      13250.0,
                  'cristiano',
                  '123456',
                  12)

print(pessoa1.nome)
print(pessoa1.funcao)
print(pessoa1.salario)
print(pessoa1.qtdFuncionarios)
if(pessoa1.autentica('cristiano','123456')):
    print(f"\nACESSO CONCEDIDO")
else:
    print(f"\nACESSO NEGADO")