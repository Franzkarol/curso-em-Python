class TaErradoError(Exception):
    pass  # excecoes personalizadas

    def testar():
        raise TaErradoError('Errado!')

    try:
        testar()
    except TaErradoError as error:
        print(f'Erro: {error}')
