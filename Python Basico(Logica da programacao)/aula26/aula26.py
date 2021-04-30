"""
Trocando o valor entre variaveis em Python
"""

# x = 10  # Luiz
# y = 'Luiz'  # 10
# x,y = y, x  # simplificando

# z = x
# x = y
# y = z

# print(f'x={x} e y={y}')

x = 10
y = 'Luiz'
z = 'Otavio'
x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')