from random import *

lista = []
num = 10

for i in range(num):
    l = randint(1,11)
    if l not in lista:
        lista.append((l))


print(lista)
