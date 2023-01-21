# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034-035
# Data: 21-01-2023
# Objetivo: OO em Python - Métodos

from Conta import Conta
from ClientePF import ClientePF

clienteNeymar = ClientePF('Neymar',
                          'Jr',
                          '123.456.789-10',
                          '12.345.678-8',
                          'Avenida Ulisses Guimarães, '
                          'n. 51, Vila do Horto, '
                          'Rio Claro, São Paulo, Brasil, '
                          '13.500-000',
                          '19-1234-6789',
                          '19-98765-4321',
                          '19-9876-5432')

cnt1 = Conta(clienteNeymar, '001-1', 1000000.0)
# print(f"{str.upper(cnt1.titular.nome)}\nSALDO: {cnt1.saldo}")
print(cnt1.extrato())

print()
print(type(cnt1))

print()
print(type(clienteNeymar))


'''
cnt1 = Conta('Neymar Jr', '001-1', 100.0, 1000.0)
print(cnt1.extrato())
print()
cnt2 = Conta('Cristiano José Cecanho', '002-1', 100.0)
print(cnt2.extrato())
print()

cnt1.transfere(cnt2, 1200.0)
print(cnt1.extrato())
print()
print(cnt2.extrato())
print()'''
