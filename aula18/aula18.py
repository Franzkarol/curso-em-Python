"""
while em Python

utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""
#
# while True:  # loop infinito
#     nome = input("Qual o seu nome? ")
#     print(f'Olá {nome}!')
#
# print('Não será executada.')
#
# x = 0
# while x < 100:
#     print(x)
#     x = x + 1
# print('Acabou!')

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break
#         print(x)
#         x = x + 1
#
#     print('Acabou!')

# x = 0  # coluna
# y = 0  # linha
#
# while x < 10:
#
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
#         y += 1
#
#         x += 1 # x = x + 1
#
# print('Acabou!')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]'im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric()  or num_2.isnumeric():
        print('Você precisa digitar um número ou sair.')
        continue

        num_1 = int(num_1)
        num_2 = int(num_2)

    # = - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')
