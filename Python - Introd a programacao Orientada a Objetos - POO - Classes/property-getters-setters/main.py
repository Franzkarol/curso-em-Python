class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, valor):
            self.__nome = valor.replace('A', '@')

        #  Getter
        @property
        def preco(self):
            return self.__preco

        #  Setter
        def preco(self, valor):
            if isinstance(valor, str):
                valor = float(valor.replace('R$', ' '))

            self.__preco = valor

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)