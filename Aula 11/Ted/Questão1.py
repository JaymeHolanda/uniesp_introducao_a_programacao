# 1) Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário

print (' digite o nome de dez clubes de futebol ')

clube=[]

for i in range(10):
    cl = str(input(f'Digite o {i+1} clube de futebol'))
    clube.append(cl)
    print('--'*20)
p = str(input(f'Qual o clube voce deseja pesquisar ? '))
if p in clube:
    print('Achei no banco de dados')
else:
    print('Não Achei no banco de dados')