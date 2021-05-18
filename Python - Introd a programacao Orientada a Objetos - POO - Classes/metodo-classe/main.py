#
# class Pessoa:
#     ano_atual = 2021
#
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def get_ano_nascimento(self):
#         print(self.ano_atual - self.idade)
#
#     @classmethod
#     def por_ano_nascimento(cls, nome, ano_nascimento):
#         idade = cls.ano_atual - ano_nascimento
#         return cls(nome, idade)
#
# # p1 = Pessoa.por_ano_nascimento('Anna', 1991)
#
# p1 = Pessoa('Anna', 30)
#
# p1.get_ano_nascimento()
# print(p1.nome, p1.idade)
#
# # print(Pessoa.ano_atual)
#
# # a instancia se chama self

"""
metodo estatico
"""

from random import random

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return  rand

p1 = Pessoa('Anna', 30)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())