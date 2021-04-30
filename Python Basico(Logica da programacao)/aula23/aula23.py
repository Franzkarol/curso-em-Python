"""
For / Else em Python
"""

variavel = ['Anna', 'João', 'Maria']

# for valor in variavel:
    # print(valor)
    # break
    # print(valor)
    # if valor.startswith('J'):
    #     print('Começa com J', valor)
    # else:
    #     print('Não começa com J', valor)

# comeca_com_j = False
# for valor in variavel:
#     if valor.lower().startswith('J'):
#         # comeca_com_j = True
#         # pass
#         continue
#         print(valor)
# if comeca_com_j:
#     print('Existe uma palavra que começa com J.')
# else:
#     print('Não existe uma palavra que começa com J.')

# correto

for valor in variavel:
    if valor.lower().startswith('J'):
        continue
    print(valor)