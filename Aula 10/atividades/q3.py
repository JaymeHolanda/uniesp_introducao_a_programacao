#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
#o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;


x=[]

while len(x) <20:
    num=int(input("Digite Numeros Inteiros para adiciona-los na lista:"))
    if num in x:
       print('Numero repetido, digite outro')
    
    elif num < 0:
        print("Digite apenas Numeros Positivos")
        
    else:
        x.append(num)
        


menval=x[0]
maval=x[0]

for valor in x:
    if valor > maval:
        maval=valor
        
print(f'O valor do maior elemento de x é {maval} e seu índice é {x.index(maval)}')

for valor in x:
    if valor < menval:
        menval=valor

print(f'O valor do menor elemento de x é {menval} e seu índice é {x.index(menval)}')