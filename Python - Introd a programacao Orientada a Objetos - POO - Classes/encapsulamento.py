"""
metodos e atributos:

public, protected, private = metodo so esta disponivel dentro do objeto

convencao:
_  = private, protected (privado mais fraco, que vc consegue acessar) (public _)
__ = private mais forte (que vc tenta acessar, mais nao consegue) (_NOMECLASSE__nomeatributo)
"""

class BaseDeDados:
    def __init__(self): #  chamado construtor
        self._dados = {}

    def inserir_cliente(self, id, nome):
            if 'clientes' not in self._dados:
                self._dados['clientes'] = {id: nome}
            else:
                self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'] [id]

bd = BaseDeDados()
bd._dados = 'Um outro valor qualquer'
print(bd._dados)

# bd.inserir_cliente(1, 'Anna')
# bd.inserir_cliente(2, 'Karol')
# bd.inserir_cliente(3, 'Franz')


# bd.apaga_cliente(2)
# bd.dados = 'Uma outra coisa'
# bd.inserir_cliente(4, 'Ronaldo')
# bd.apaga_cliente(2)

# bd.lista_clientes()

# print(bd.dados)