#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.
cadastros=[]

botao=1000
while botao != 0:
    print('Digite 1 para cadastrar um novo usuário')
    print('Digite 2 para imprimir todos os usuarios')
    print('Digite 0 para sair')
    botao=int(input('Digite a opçao desejada: '))

    if botao==1:
        #entrada dos dados
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        email = input("Digite o seu e-mail: ")
        
        #Folha de Cadastro
        dados = [nome, idade, email]
        
        #Guardando a folha na pasta
        cadastros.append(dados)
   
    elif botao==2:
        for pessoas in cadastros:
            print(pessoas)

    elif botao==0:
        print('Já foi tarde!!!')

    else:
        print('Digite um numero válido!')