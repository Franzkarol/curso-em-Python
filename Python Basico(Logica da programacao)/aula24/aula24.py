"""
Split, Join, Enumerate em Python

* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate = Enumerar elementos da lista # list / iteraveis
"""

# Split = ela dividi o valor que eu quiser
# string = " O Brasil é o país do futebol, o Brasil é penta."
# lista = string.split(' ')
# lista_2 = string.split(',')
#
# print(lista)
# print(lista_2)
#
# palavra = ''
# contagem = 0
#
# for valor in lista:
#     # print(valor)
#     # print( f'A palavra {valor} apareceu {lista.count(valor)}x na frase.' )
#     qtd_vezes = lista.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# Join
# string = 'O Brasil é penta.'
# lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

# Enumerate

# string = 'O Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor)

# lista = [
    # [1,2],
    # [3,4],
    # [5,6],

#     [0,'Anna'],
#     [1, 'João'],
#     [2, 'Maria'],
# ]
# for v in lista:
    # print(v)
    # print(v[0])
    # print(v[0], v[1])

# for indice, nome in lista:
#     print(indice, nome)

lista = ['Anna', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
