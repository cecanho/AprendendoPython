# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 062
# Data: 23-04-2023
# Objetivo: Instrução finally

def divide(n1, n2):
    try:
        print(f"Resulado {n1} / {n2} = {n1 / n2}")
    except ZeroDivisionError:
        print(f"Divisão por ZERO")
    finally:
        print("executando o finally")

if __name__ == '__main__':
    divide(2, 1)
    divide(2, 0)
    divide('2', '1')
