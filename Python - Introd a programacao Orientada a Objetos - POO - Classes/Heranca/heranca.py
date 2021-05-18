from classes import *

"""
Associaçao - Usa | Agregaçao - Tem | Composiçao - E dono | Herança
"""

c1 = Cliente('Anna', 30)
c1.falar()
c1.comprar()
c1.estudar()

# print(c1.nome)
a1 = Aluno('Karol', 54)
a1.falar()
a1.estudar()
a1.comprar()
# print(a1.nome)

p1 = Pessoa('Joao', 34)
p1.falar()