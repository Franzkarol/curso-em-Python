# utilizar o modulo os

import os

caminho_procura = '/media/anna/Externo/serie'
termo_procura = '09'

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'

# caminha entre os arquivos no sistema
conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
  for arquivo in arquivos:
    if termo_procura in arquivo:
      try:
            conta += 1
            caminho_completo = os.path.join(raiz, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
            tamanho = os.path.getsize(caminho_completo)
    
            print()
            print('Encontrei o arquivo:', arquivo)
            print('Caminho:', caminho_completo)
            print('Nome', nome_arquivo)
            print('Extensão:', ext_arquivo)
            print('Tamanho:', tamanho)
        except PermissionsError as e:
            print('Sem permissões.')
      except FileNotFoundError as e:
          print('Arquivo não encontrado')
      except Exception as e:
          print('Erro desconhecido:', e )

print()
print(f'{conta} arquivo(s) encontrado(s)')
        # print(tamanho)
        # print(nome_arquivo, ext_arquivo, sep='---')
        # print(arquivo)
        # print(caminho_completo)
