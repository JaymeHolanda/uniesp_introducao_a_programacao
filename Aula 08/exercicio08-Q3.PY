#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.

n1 = int (input("Digite um número inteiro aqui   "))
n2 = int (input("Digite outro número inteiro aqui   "))

a = n1 + n2 
print(f'A adição de {n1} mais {n2} é igual a {a}')

s = n1 - n2 
print(f'A Subtração de {n1} menos {n2} é igual a {s}')

m = n1 * n2
print(f'A Multiplicação de {n1} x {n2} é igual a {m}')

d = n1 / n2
print(f'A Divisão de {n1} / {n2} é igual a {d}')

p = n1 ** n2
print(f'A Potência de {n1} elevado a {n2} é igual a {p}')


