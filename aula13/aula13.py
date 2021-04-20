"""
Operadores Lógicos
and, or, not
in e not in
"""
#
# In[2]: a = 2
# In[3]: b = 2
# In[4]: c = 3
#
# In[5]: a == b and b < c
# Out[5]: True
# Int[6]: a == b or b < c
# Out[6]: True
#
# Int[7]: not a == b and not b < c

# (Verdadeiro e  False) = False
# comparacao1 and comparacao

# Verdadeiro ou Verdadeiro
# comp1 OR comp2
#
# a = 2
# b = 3
#
# if not b > a:
#     print('B é maior do que A.')
# else:
#     print('A é maior do que B.')

# a = ''
# b = 0
#
# if not a:
#     print('Por favor, preencha o valor de A.')

# nome = 'Anna Karolina'

# if 'a' in nome:
#     print("Existe")
# else:
#     print("Não existe.")
#
# if 'asdas' not in nome:
#     print("Executei.")
# else:
#     print("Existe o texto.")

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'anna'
senha_bd = '123456'

if usuario == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')

