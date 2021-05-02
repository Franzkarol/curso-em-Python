# nome = input('Qual o seu nome? ')
# print(nome or None or False or 0 or 'Você não digitou nada.' or 'Outra coisa')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Anna'

variavel = a or b or c or d or e or f or g

if a:
    variavel = a
elif b:
    variavel = b