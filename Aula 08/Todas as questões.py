#ATIVIDADE DA AULA 08 - Atividade Avaliativa

#ALUNOS: Jayme Holanda Aguiar e Felipe Cavalcanti 



#Questão 01 

a = float(input("Qual o valor de A ?    "))
b = float(input("Qual o valor de B ?    "))
c = float(input("Qual o valor de C ?    "))

d = b**2 - 4 * (a * c )

x1 = (-b + (d**0.5) ) / (2*a)
print (x1)

x2 = (-b - (d**0.5) ) / (2*a)
print (x2)

#Questão 02

x1 = float(input(" Digite o valor de X1 "))
x2 = float(input(" Digite o valor de X2 "))
y1 = float(input(" Digite o valor de Y1 "))
y2 = float(input(" Digite o valor de Y2 "))

d1 =  (x2 - x1)**2
d2 = (y2 - y1)**2 
d3 = (d1 + d2)**0.5  

print(f'Sua resposta é {d3:.3f}')

#Questão 03 

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

#Questão 04

altura = float(input("Qual sua altura em Metros ?   "))
peso = float(input("Qual o seu peso em KG ?    "))
imc = peso / (altura**2) 

if imc > 30: 
    print('Obeso')
elif imc > 25 and imc >=30:  
    print('acima do peso')
elif imc <= 25 and imc >= 18.5: 
    print('Peso Normal')
else:
    print('Abaixo do peso')


#Questão 05 

lista1=[]
lista2=[]
lista3=[]
lista4=[]

numeros=1000

while numeros >=0:

    numeros=float(input('Digite numeros aleatorios (positivos e negativos):'))
    
    if numeros >=0 and numeros <=25:
        lista1.append(numeros)
        
    elif numeros >=26 and numeros <=50:
        lista2.append(numeros)
        
    elif numeros >=51 and numeros <=75:
        lista3.append(numeros)
        
    elif numeros >=76 and numeros <=100:
        lista4.append(numeros)

    elif numeros > 100:
        numeros

    else:
        print('a quantidade de numeros entre:')
        print(f'0-25 = {len(lista1)}')
        print(f'26-50 = {len(lista2)}')
        print(f'51-75 = {len(lista3)}')
        print(f'76-100 = {len(lista4)}')

#Questão 06 

n = int(input("Digite um número: "))
contador = n
fatorial = 1

print("Calculando {}! = ".format(n), end="")
while contador > 0:
    print("{} ".format(contador), end="")
    print(' x ' if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1
print("{}".format(fatorial))