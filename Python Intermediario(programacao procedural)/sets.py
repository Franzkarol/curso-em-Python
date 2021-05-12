"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference (elementos que estao nos dois sets)
"""

l1 = ['Luiz', 'Joao', 'Maria']
l2 = ['Joao', 'Maria', 'Maria',
        'Luiz', 'Luiz',]

if set(l1) == set(l2):
    print('L1 e igual a L2')
else:
    print('L1 e diferente de L2')