# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034-035-036-037
# Data: 29-01-2023
# Objetivo: OO em Python - Agregação/Composição

from Conta import Conta
from ClientePF import ClientePF
from Endereco import Endereco

endereco = Endereco('n. 1',
                    'Fundos',
                    'Avenida Ulisses Guimarães',
                    'Vila indaiá',
                    'Rio Claro',
                    'SP',
                    'Brasil',
                    '13500-000')

cliente1 = ClientePF('João', 'Oliveira', '111111111-11', '12345678-9', endereco, '3333-3333', '99999-9999', '3333-3333')
cliente2 = ClientePF('José', 'Azevedo', '222222222-22', '12345679-9', endereco, '3333-3333', '99999-9998', '3333-3333')

conta1 = Conta(cliente1, '123-4', 1000.0)
conta2 = Conta(cliente2, '123-5', 1000.0)

conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere(conta2, 200.0)

print(type(conta1.titular))
print(conta1.extrato())


conta1.historico.imprime()
print()
print(conta2.extrato())
conta2.historico.imprime()