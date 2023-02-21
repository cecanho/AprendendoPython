# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 044
# Data: 21-02-2023
# Objetivo: OO em Python - Exercícios da pág. 123-125 (130-133)

'''
1. Adicione o modificador de visibilidade privado (dois underscores: __ ) para cada atributo e método
da sua classe Conta .
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite
Tente criar uma Conta e modificar ou ler um de seus atributos "privados". O que acontece?

2. Sabendo que no Python não existem atributos privados, como podemos modificar e ler esses
atributos? É uma boa prática fazer isso?
Dica: teste os comandos print(conta.__numero) e print(conta._Conta__numero . O que ocorre?

3. Modifique o acesso para 'protegido' seguindo a convenção do Python e modifique o prefixo __ por
apenas um underscore _ . Crie métodos de acesso em sua classe Conta através do decorator
@property .
class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

4. Crie novamente uma conta e acesse e modifique seus atributos. O que mudou?
Dica: tente os comandos na seguinte ordem: print(conta._numero) , conta._numero= '50' e
print(conta._numero) . O que ocorre?

5. Modifique sua classe Conta de modo que não seja permitido criar outros atributos além dos
definidos anteriormente utilizando __slots__ .
class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

6. (Opcional) Adicione um atributo identificador na classe Conta . Esse identificador deve ter um
valor único para cada instância do tipo Conta . A primeira Conta instanciada tem identificador 1, a
segunda 2, e assim por diante.
class Conta:
      identificador = 1
      def __init__(self, numero, titular, saldo, limite=1000.0):
            self.identificador = Conta.identificador
            Conta.identificador += 1
'''

# Exercicio 01

from Conta import Conta

conta = Conta('001-1', 'Pingo', 120.0)
# conta.__saldo += 10.0
# print(f"Saldo: {conta.__saldo}")

# Exercicio 02
# print(conta.__numero)
# print(conta._Conta__numero)

# Exercicio 03, 04 e 05

conta._saldo = 150.0

print(f"N. Conta: {conta.numero}\n"
      f"Titular: {conta.titular}\n"
      f"Saldo: {conta.saldo}\n"
      f"Limite: {conta.limite}\n")

print(conta._numero)
conta._numero= '50'
print(conta._numero)

# Exercicio 06
conta2 = Conta('51', 'Caninha', 10.0)
print(f"Conta 1: {conta.identificador}")
print(f"Conta 2: {conta2.identificador}")