# lists, tuples, str -> Sequences -> Iteravel
nome = ' Luiz Otavio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o FOR')

for letra in gerador:
    print(letra)

print('Olha outro FOR')

for letra in gerador:
    print(letra)

print(next(gerador))


# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
# except:
#     pass
#
# print('Cade os valores? ')
# for valor in iterador:
#     print(valor)


# for letra in nome:
#     print(letra)
#
# print('#' * 80)
#
# for letra in nome:
#     print(letra)
#
# print(nome)