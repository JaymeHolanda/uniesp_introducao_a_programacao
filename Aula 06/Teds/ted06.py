#i = 1 
#while i < 10: 
 #   print(i)
  #  i += 1

#captains = ['calos', 'alberto', 'Raissa']
 
#for x in captains: 
    #print(x)

#for x in 'banana': 
 #   print(x)

#fruits = ["apple", "banana", "cherry"]
#for x in fruits: 
 #   print(x)
  #  if x == 'banana':
   #     break

#lista = ['',''] /  
# for nome in lista

#Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
#divididos por 11, produzam o resto igual a 5.



cadastros = []
botao = 1000

while botao !=0:
  print('Digite 1 para cadastrar um novo usuário')
  print('Digite 2 para imprimir todos os usuários')
  print('Digite 0 para sair do programa de Cadastro')

  botao = int(input('Digite a opção desejada     '))

  if botao == 1: 
    nome = input("Qual o seu nome ?   ")
    idade = input("Qual o seu idade ?   ")
    email = input("Qual o seu email ?   ")
  #Folha de Cadastros:
    dados = [nome,idade,email]
  #Guardando a folha na pasta
    cadastros.append(dados) 
  
  elif botao == 2:
    for x in cadastros: 
      print(x)
  elif botao == 0:
    print("Obrigado por acessar este software!")
  else:
    print('Digite um número válido')