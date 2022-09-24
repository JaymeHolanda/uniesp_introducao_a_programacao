#.1 As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

# MAÇÃS = 1.30 CADA SE COMPRADAS MENOS 12 

# MAÇÃS = 1.00 CADA SE COMPRADAS PELO MENOS 12 

m = int(input('Quantas maçãs você comprou ?    '))
m1 = m * 1.30
m2 = m * 1

if m >= 12:
    print(f' Você pelo menos 12 maçãs. Então o preço é R$: {m2:.3}')
elif m < 12: 
    print(f'Você comprou doze ou mais maças. Então o Preço é R$: {m1:.3}')