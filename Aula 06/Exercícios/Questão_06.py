#Seja criativo ao desenvolver este programa.
#a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
#b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
#c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
#d. Modifique sua lista, substitua os desistentes por novos convidados.
#e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados =  ['Carlos', 'Pedro', 'Lucas', 'Luiza']

for nome in convidados:
    print(f" Opa! Tudo bem {nome} ? Gostaria de sair hoje?")  

print("Luiza. Não terei como sair hoje") 

convidados[4]= 'Lucas'

for nome in convidados:
    print(f"Ei {nome.upper()}, Vamos sair hoje?")