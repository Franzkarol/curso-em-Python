# Introdução à formatação de Strings

nome = 'Anna Karolina'
idade = 30  # int
altura = 1.58  # float
e_maior = idade > 18  # bool
peso = 56
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'texto')  #f string
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # valores formatados
print('{0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
