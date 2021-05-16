"""
Uso de try e except como condicional
"""

# numero = int(input('Digite um numero:   '))
# print(numero * 5)

# numero = float(input('Digite um numero: '))
# print(numero * 5)

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input('Digite um numero: '))

    if numero is None:
        print('Erro: isso nao e um numero')
    else:
        print(numero * 2)