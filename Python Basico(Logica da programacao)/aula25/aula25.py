"""
Desempacotamento de lista Python
"""

lista = ['Anna', 'João', 'Maria', 1,2,3,4,5]

# n1, n2, *outra_lista, ultimo_da_lista = lista
#
# print(n2)
# print(n1, n2)
# print(n1, n2, outra_lista)
# print(ultimo_da_lista)

n1, n2, *_ = lista

print(n1, n2)