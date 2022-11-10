#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.


lista_times = []

print("_Adiciona 10 nomes de times na lista_")

clube = str(input("Digite o nome de um clube para adicionar a lista: "))
lista_times.append(clube)

while len(lista_times) <= 9:
    clube = str(input("Digite o nome de mais um clube: "))
    if clube in lista_times:
        print(" Esse clube já foi adicionado. Tente outro! ")
    else:
        lista_times.append(clube)
    
print("  A lista de clubes foi preenchida! ")

pesquisa = str(input("Digite o nome do clube que deseja procurar: "))

if pesquisa in lista_times:
    print(f"Encontrado. O clube {pesquisa} encontra-se na lista. ")
else:
    print(f" NÃO ACHEI. O clube {pesquisa} não foi encontrado na lista.")

