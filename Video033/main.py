# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034
# Data: 14-01-2023
# Objetivo: OO em Python - Métodos

from Conta import Conta

cnt1 = Conta('Neymar Jr', '001-1', 100.0, 1000.0)
print(cnt1.extrato())
print()
cnt2 = Conta('Cristiano José Cecanho', '002-1', 100.0, 1000.0)
# print(cnt1.saldo)
'''
print(cnt1.extrato())

cnt1.setLimite(1500.0)

print()
print(cnt1.extrato())

cnt1.setTitular('Pingo Cecanho')
cnt1.titular = 'Alterado Cecanho'
print()
print(cnt1.extrato())

cnt1.saca(2000.0)
'''

cnt1.transfere(cnt2, 100.0)

print(cnt1.extrato())
print()
print(cnt2.extrato())