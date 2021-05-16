#except pega qualquer tipo de erro

# try:
#     print(a)
# except:
#     print('Erro')

# try:
#     print(a)
# except NameError as erro:
#     print('Erro:', erro)

try:
    a = 1/0
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele. ')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave. ')
except Exception as erro:
    print('Ocorreu um erro inesperado. ')
else:
    # print('Seu codigo foi executado com sucesso!')
    pass
    print(a)
finally:
    a = ' '
    # print('Finalmente. ')

# print('Bora continuar...')

print(a)