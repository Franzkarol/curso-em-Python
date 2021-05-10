"""
Funções (def) em Python - *args **kwargs 

Word argumentos 

Os argumentos posso utilizar dentro das funções

Eu chamo a função e coloco o nome da função e passo os argumentos citando o valor do 2 a 1.

Uma coisa que eu não posso fazer aqui por exemplo se eu tivesse mais um argumento aqui por exemplo A6, só que se ta vendo aqui que o Pai já está gerando erro aqui pra mim, isso está acontecendo por aqui, é o seguinte a partir do momento padrão a partir do momento que o certo um valor padrão para o argumento os proximos que vem depois dele tambem precisam de um padrão. 

O argumento que eu quero que ela retorna pq ela retorna e eu posso utilizar um ou mais argumento se eu quiser por exemplo eu quero que ela retorne um nome ou A6 aqui e ai se eu der um print ela vai ter uma 
"""

# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#   print(a1, a2, a3, a4, a5, nome, a6)
#   return nome, a6

# func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
# print(var[0], var[1])

# def func(*args):
#   print(args)
#   print(args[0])
#   print(args[-1])
#   print(len(args))

# func(1, 2, 3, 4, 5)
# n1, n2, *n = lista
# print(*lista, sep='-')

# def func(*args, **kwargs):
  # for v in args:
    # print(args)
    # print(kwargs['nome'], kwargs['sobrenome'])

    # nome = kwargs.get('nome')
    # print(nome)

    def func(*args, **kwargs):
      print(args)

      idade = kwargs.get('idade')

      if idade is not None:
        print(idade)
      else:
        print('Idade não existe.')

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)