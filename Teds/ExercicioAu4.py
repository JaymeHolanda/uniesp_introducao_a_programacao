#Estruturas de Seleção

#1. #Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

#n = float (input('Digite um número ..  '))

#if n > 10:
    #print('Seu valor é 10 ou maior do que dez')
#elif n < 10:
    #print('Seu valor é menor do que 10.')
#else:
    #print('Seu valor é 10')


#Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

#n = float(input('Digite um valor aqui   '))
#if n >= 0:
    #print('Seu número é positivo')
#else:
    #print('Seu número é negativo')

#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

#m = int(input('Quantas maças você comprou ?   ') )
#if m >= 12:
    #print(f'O total de suas compras deram: R$ {m*1}')
#elif m < 12:
   #print(f'O total de suas compras foram de: R$ {m*1.30:.2f}')