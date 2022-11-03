#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

clube = []

while len(clube) <=10:
    nomes= input('Digite um clube de futebol: ')
    clube.append(nomes)
leitura = input('qual clube de futebol você deseja buscar? ')
if leitura in clube:
    print('Achei!')
else:
    print('Não achei!')
print(clube)