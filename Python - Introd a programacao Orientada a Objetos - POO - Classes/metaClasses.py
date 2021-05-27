"""
Em Python tudo é um objeto: incluindo classes
Mateclasses são as "classes" que criam classes.
type é uma metaclasse (!!!!?????)
"""

# class A:
#     attr = 'Valor' # aqui são os models


#  são instancias da classes

# a = A()
# b = A()
# c = A()

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
             return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Oi, vc precisa criar o método b_fala em {name}')

        print(namespace)
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):  # bibliotecas
    def fala(self):
        self.b_fala()

class B(A):  # interface
    # def b_fala(sel):
    #     print('Oi')
    teste = 'Valor'
    pass
    def sei_la(self):
        pass

# b = B()
# b.fala()