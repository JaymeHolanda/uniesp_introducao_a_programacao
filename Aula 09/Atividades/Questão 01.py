#Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.

dicionario={
    'Primeiro_nome': 'Jayme',
    'Sobrenome': 'Holanda',
    'Idade': '26',
    'Cidade':'João Pessoa'
}

for info in dicionario.items():
    print(info)
