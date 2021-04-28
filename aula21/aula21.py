"""
For in em Python
Interando strings com for
Função range(start=0, stop, step=1)
"""

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c +=

#simplificando
# for n, letra in enumerate(texto):
#     print(n, letra)
#

#Função range
# Ela recebe três paramentros: start(argumento de inicio, onde quero que ela inicie), stop, step( de quantas casas ele vai pular)
# for n in range(20, 10, -1):
#     print(n)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

    print(nova_string)

# continue = pula paa o proximo laço
# break = termina o laço, ela para