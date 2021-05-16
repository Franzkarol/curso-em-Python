"""
Combinations, Permutations e Product - Itertools
Combinaçao - Ordem nao importa
Permutaçao - Ordem importa
Ambos nao repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio']

for grupo in  combinations(pessoas, 3):
    print(grupo)