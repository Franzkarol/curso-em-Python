# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise
#         # return False
#
# try:
#     print(divide(2,1))
# except ZeroDivisionError as error:
#     print(error)

# print(divide(2,1))  # o numero nao pode ser dividido por 0

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 nao pode ser 0.')
    return n1 / n2

try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print('Voce esta tentando dividir por 0.')
    print('Log:', error)