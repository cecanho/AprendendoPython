# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 042
# Data: 12-02-2023
# Objetivo: OO em Python - Atributos de classe
# Alterações baseadas na pág. 120-121 (127-128)

class Conta:

    _total_contas = 0

    def __init__(self):
        type(self)._total_contas += 1

    @classmethod
    def get_total_contas(cls):
        return cls._total_contas