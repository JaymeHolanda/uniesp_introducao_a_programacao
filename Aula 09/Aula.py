#O que fazer quando queremos realizar 


gatilho=0.8
lista_vendedores=[0.8,0.25,0.5,1.2,1.0]

result_soma=0

for vendedor in lista_vendedores:
    result_soma=result_soma+vendedor


#Result Soma ao final = 3.75

media=result_soma/len(lista_vendedores)

maior_vendedor=0
menor_vendedor=1000

if media >= gatilho:
    print('Campanha válida! Equipe de parabens!!')
    for vendedor in lista_vendedores:
        if vendedor > maior_vendedor:
            maior_vendedor=vendedor

        elif vendedor<menor_vendedor:
                menor_vendedor=vendedor
        
        else:
            print('O vendedor é igual, perdeu a vez')

else:
    print('A campanha foi um desastre!')