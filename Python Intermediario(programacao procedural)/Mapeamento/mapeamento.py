from map import produtos, pessoas, lista

# precos = map(lambda p: p['preco'], produtos)

# for preco in precos:
    # print(preco)

    # print(produtos)
#
# def aumenta_preco(p):
#     p['preco'] = p['preco'] * 1.05
#     return p
#
# # precos = map(aumenta_preco, produtos)
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

# nomes = map(lambda p: p['nome'], pessoas)
#
# for pessoa in pessoas:
#     print(pessoa)

def aumenta_idade(p):
    p['nova_idade'] = int(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)