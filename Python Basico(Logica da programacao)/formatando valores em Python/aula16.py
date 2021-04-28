"""
Formatando valores com modificadores

:s - texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuante (float)
:. (NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ⁾(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^- Centro
"""

# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print(  '{:.2f}'.format(divisao) )
# print( f'{divisao:.2f}')

# num_1 = 1
# print(f'{num_1:0>10}')
#
# num_2 = 1150
# # print(f'{num_2:0>10}')
# print(f'{num_2:0>10.2f}')

# nome = 'Anna Karolina'
# print( 50-len(nome))
# print(f'{nome:#^50}')

# nome = "Anna Karolina"
# sobrenome = 'Franz'
# nome_formatado = '{0:$⁵0} {1:#⁵0}'.format(nome, sobrenome, qualquer)
# print(nome_formatado)

nome = 'Anna Karolina'
# nome = nome.lower()
# nome = nome.ljust(10, '#')
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas