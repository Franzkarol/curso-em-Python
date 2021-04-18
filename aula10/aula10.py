"""
Input: Entrada de dados do usuário
"""

# nome = input("Qual seu nome? ")  # sempre da espaço
# print(f'O usuário digitou {nome} e o tipo da variavel é '
#       f'{type(nome)}')
#
# nome = input("Qual o seu nome? ")
# idade = input("Qual a sua idade? ")

# ano_nascimento = 2021 - idade  # não é possivel realizar uma conta entre um int e string
# ano_nascimento = 2021 - int(idade)  #fazendo um cast ou seja conversão uma string para um numero inteiro

# print()  # print vazio ele pula uma linha
# print(f'{nome} tem {idade} anos. '
#       f'{nome} nasceu em {ano_nascimento}.')

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro numero: ')
#
# print( numero_1 + numero_2 )  # ele não faz a soma, ele concatenou

numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro numero: ')
numero_2 = int(numero_2)

# print( numero_1 + numero_2 )
print( numero_1 ** numero_2)

