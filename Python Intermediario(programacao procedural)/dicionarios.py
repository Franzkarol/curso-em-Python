"""
No dicionario vc controla o indice, formalmente tambem chamado de chave ou seja o dicionario tem uma estrutura de dados que suporta o papel
de chave e valor

Geralmente vc vai ve strings, mais eu posso utilizar numeros, posso utilizar tuplas(so pode valores mutaveis)

A partir do momento que eu acessei o valor de uma chave aqui dentro, um item imutavel ele ja mudou nas duas listas aqui

Entao quando a gente fala Shell ou Coppe e que a gente pode alterar os valores aqui dentro.

Porem pra vc criar uma copia real de um dicionario vai precisar utilizar um modulo chamado copia

Se vc utilizar a funçao deepcopy que ja vem no dicionario, vc esta copy criando uma copia arrasa
de qualquer elemento dentro, por exemplo se vc tem um dicionario dentro de um dicionario, esse dicionario secundario
vair poder ser alterado, exceto o dicionario filho vai poder ser alterado no seu clone, na sua copia do seu dicionario.

Se vc tiver uma lista tambem ha uma coisa que nao vai alterar o plano seu

"""
# d1 = { 'chave' = 'valor'}

# d1 = {'chave1': 'valor da chave'}
# d1['nova chave'] = 'Valor da nova chave'
#
# print(d1['chave1'])

# d1 = dict(chave='Valor da chave', chave2='Valor da outra chave')
# d1['nova chave'] = 'Valor da nova chave'
#
# print(d1)

# d1 = {
#     'chave1': 'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla',
# }
#
# # interar
#
# for k, v in d1.items():
#     print(k, v)

# for k in d1.items():  # acessando a chave e o valor
#     print(k[0], k[1])

# for v in d1.values():
#     print(v)

# print(len(d1))

# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())

# del d1['str']  # apagando a chave
#
# print(d1)

# d1['nomedachave'] = 'Agora ela existe.'

# d1.update({'nova_chave': 'novo_valor'})
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))


# if d1.get('nomedachave') is not None:
#     print(d1.get('nomedachave'))

# print(123)

# d1['naoexiste'] = 'Agora existe.'
# if 'naoexiste' in d1:
# print(d1['naoexiste'])
#
# print('OI')

# clientes = {
#     'cliente1' : {
#       'nome' : 'Anna',
#         'sobrenome': 'Franz',
#     },
#     'cliente2' : {
#       'nome' : 'Karolina',
#         'sobrenome': 'Vieira',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# import copy
#
# d1 = { 1: 'a', 2: 'b', 3: 'c', 'd': ['Anna', 'Franz']}
# # v = d1   # alterando, quando vc usa o sinal de = vc nao ta criando novo objeto
#
# # v[1] = 'Anna'
#
# v = copy.deepcopy(d1)
# v[1] = 'Anna'
# v['d'][0] = 'Joao'
#
# print(v['d'][0])
#
# print(d1)
# print(v)

d1 = {
    1: 2,
    2: 3,
    3: 5,
}

d2 = {
    'a': 'b',
    'c': 'd',
}

d1.update(d2)
print(d1)