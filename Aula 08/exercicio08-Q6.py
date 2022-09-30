# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. 
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

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