mtz = [
    [78,90,100],
    [56,77,93],
    [10,4,73]
]

for linha in range(len(mtz)):
    for coluna in range(len(mtz[linha])):
        if linha == coluna:
            print(mtz[linha][coluna])

        if (mtz[linha][coluna] % 2) == 0:  # se o resto da divisão sobrar zero. Ele é par.
            print(f'{mtz[linha][coluna]} --> é par')
        else:
            print(f"{mtz[linha][coluna]} --> é impar")

# Como sabemos a Matriz tem uma lista, que por sua vez tem outra lista dentro. 
#Logo precisamos de um For dentro de um For.
