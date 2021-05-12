"""
Basicamente pra treinar unir as coisas que a gente aprendeu ate nesse momento

A gente vai utilizar os laços formam a estrutura de repetiçao
"""

print('Texto explicativo.')
print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto e 2+2? ',
        'resposta': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto e 3*2? ',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
}

print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH!!! Voce acertou!!!!')
        respostas_certas += 1
    else:
        print('IXIII!! Voce errou!!!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')