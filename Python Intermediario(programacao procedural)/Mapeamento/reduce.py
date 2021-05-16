from dados import produtos, pessoas, lista
from functools import  reduce

# soma_lista = reduce(lambda acumulador, i: i + acumulador, lista, 0)
# print(soma_lista)

# soma_precos = reduce(lambda acumulador, p: p['preco']  + acumulador, produtos, 0)
# print(soma_precos / len(produtos))

soma_idades = reduce(lambda acumulador, p: acumulador + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))