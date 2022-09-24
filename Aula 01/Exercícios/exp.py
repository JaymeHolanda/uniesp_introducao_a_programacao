idade = int(input('Qual sua idade ?   '))
print(f'Você tem {idade}')

if idade >= 18: 
    print('Você pode pode entrar nessa festa')

while idade < 18: 
    print("você não pode entrar nessa festa")
    idade +=1