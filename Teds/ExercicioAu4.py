#Estruturas de Seleção

#1. #Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

n = float (input('Digite um número ..  '))

if n > 10:
    print('Seu valor é 10 ou maior do que dez')
elif n < 10:
    print('Seu valor é menor do que 10.')
else:
    print('Seu valor é 10')


#Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

n = float(input('Digite um valor aqui   '))
if n >= 0:
    print('Seu número é positivo')
else:
    print('Seu número é negativo')

#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

m = int(input('Quantas maças você comprou ?   ') )
if m >= 12:
    print(f'O total de suas compras deram: R$ {m*1}')
elif m < 12:
   print(f'O total de suas compras foram de: R$ {m*1.30:.2f}')

#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

n1 = float(input('Digite um número aqui  '))
n2 = float(input('Digite outro numero aqui   '))

if n1 > n2:
   print(n1)
    
else:
    print(n2)

# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

n1 = int(input('Digite um valor aqui   '))
n2= int(input('Digite outro valor aqui   '))

if n1 > n2:
    print(f'{n2},{n1}')
elif n1 < n2:
    print(f'{n1},{n2}')

#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numerodaconta = int (input('Digite o número da sua conta:      '))
saldo = int(input('Qual o seu saldo ?    '))
débito = int(input('Qual o seu débito?    '))
crédito = int(input('Qual o seu credito ?   '))
saldoatual = saldo - débito + crédito

if saldoatual > 0: 
    print(f'seu saldo atual é de {saldoatual} Saldo Positivo.')
elif saldoatual <= 0: 
    print(f'O seu saldo atual é de {saldoatual}. Saldo Negativo.')

#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'

estoque = int(input('Qual a quantidade em estoque atualmente ?     '))
estoquemaximo = int(input('Qual a quantidade máxima do seu estoque ?   '))
estoqueminimo = int(input('Qual a quantidade minima do seu estoque ?   '))
mediaestoque = (estoquemaximo + estoqueminimo) / 2

if estoque >= mediaestoque:
    print('Não comprar estoque no momento!')
elif estoque < mediaestoque:
    print('Comprar de estoque necessária!')