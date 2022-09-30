#Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.
n = int(input("Quantos números: "))

i = 0
a = 0
b = 0
c = 0
d = 0

while i > n:
  
    numero = int(input("Insira número:"))
    i = i+ 1
    print(i)
    if n > 0: 
        break


    if n >= 0 and n <= 25: 
        a = a+ 1

    elif n >= 26 and n <= 50:
        b = b+ 1

    elif n >= 51 and n <= 75:
        c = c+ 1
    elif n >= 76 and n <= 100:
        d = d+ 1

print("Intervalo1: ",a)
print("Intervalo2: ",b)
print("Intervalo3: ",c)
print("Intervalo4: ",d)



