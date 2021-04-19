"""
Operadores Relacionais - Aula 12

== igualdade > maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= dirente
"""

# Os operadores relacionais são feitos justamente para realizar comparações entre coisa certo
# Desses aqui qualquer um desses operadores sempre que eles forem executados a expressao vai inteira e vai retornar um valor booleano


# print(2 == 2)  # utilizando dois sinais de iguais a dois pensando seguinte sempre que utilizar um sinal de igual, afirmando que dois é igual a dois.

# num_1 = 2  # int
# num_2 = 2  # int
#
# expressao = (num_1 == num_2)
#
# print(expressao)

# var_1 = 'Luiz'
# var_2 = 'Otávio'
#
# expressao = (var_1 != var_2)
#
# print(expressao)

nome = input('Qual o seu nome? ')
idade = input('QUal a sua idade? ')

idade = int(idade)

idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

# Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo.')