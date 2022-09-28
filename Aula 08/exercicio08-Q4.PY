#O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

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