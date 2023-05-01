from collections import deque

fila = deque()
fila.append('1')
fila.append('2')
fila.append('3')
print(len(fila)) #saída: 3
fila.pop() #exclui elemento da direita
fila.append('3') #adiciona elemento na direita
fila.popleft() #exclui elemento da esquerda
fila.appendleft('1') #adiciona elemento na esquerda
fila.appendleft('4')
print(len(fila)) #saída: 3