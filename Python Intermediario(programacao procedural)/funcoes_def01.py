# def funcao():
#     print('Hello World')
#
#     funcao()
#     funcao()
#     funcao()
#     funcao()
#
#     print('Hello Word')
#     print('Hello Word')
#     print('Hello Word')
#     print('Hello Word')


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)