"""
mover, copiar e apagar arquivos
"""

import os
import shutil

caminho_orginal = 'C:\Users\55489\Documents\curso-em-Python'
caminho_novo = 'C:\Users\55489\Documents\serie2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        # print(old_file_path)

        shutil.move(old_file, new_file_path)
        print(f'Arquivo {file} movido com sucesso!')