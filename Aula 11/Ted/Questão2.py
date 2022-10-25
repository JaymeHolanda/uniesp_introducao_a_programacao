#2) Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

import random
n = int(input('Digite um número'    ))
v=[]

for i in range(30):
    t = random.randint(0,10)
    v.append((t))

rt=v.count(n)
print(v)
print(rt)