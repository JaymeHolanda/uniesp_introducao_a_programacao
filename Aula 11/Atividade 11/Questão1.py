#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

clubes = []

for i in range(10):
    clube=input('Digite o novo clube') 
    clubes.append(clube)

clube_pesquisar = input('Digite o novo clube:    ')

for c in clubes: 

    if clube_pesquisar.upper() == str(c).upper():
        print('Achei!')

    else: 
        print('Não achei! ')