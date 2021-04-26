"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""

#positivos [012345678]
texto        =  'Python s2'

#negativos -[987654321]

# print( texto[9]  )

# url = 'www.google.com.br/'
#
# print( url[:-1])

# nova_string = texto[-9]
# print(nova_string)

print( len(texto) )

for letra in texto:
    print(letra)