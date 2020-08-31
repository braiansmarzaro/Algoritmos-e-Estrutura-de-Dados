"""Deivid Braian Smarzaro. Eng Metal 2020.1"""
"""Informações:
a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3.6 litros, que custam R$ 25,00."""
from math import ceil

area = float(input("Digite a área a ser pintada em m²:"))
litro = area / 6
litro *= 1.1  # 10% exigido pela questão
print(f'Você precisará de {litro:.2f} litros de tinta para pintar {area}m²')
lata = litro / 18  # lata tem 18L de tinta
galao = litro / 3.6  # Galao tem 3.6 litros
if lata < 1:
    lata = 1
if galao < 1:
    galao = 1
lata = ceil(lata)
galao = ceil(galao)
valorlata = 80 * lata  # Lata custa R$80
valorgalao = 25 * galao  # galao custa R$25
print(f'Caso queira apenas latas de tinta, você gastará {lata:.2f} latas de tinta, que custarão R${valorlata:.2f}')
print(f'Caso escolha o galão de tinta, você gastará {galao:.2f} galões de tinta, que custarão R${valorgalao:.2f}')

# Misturando latas e galões
latas = litro // 18
resto = litro - latas * 18
galoes = ceil(resto / 3.6)

# Corrige bug em que o programa pode escolher uma opção mais cara para economizar tinta
if galoes == 4 or galoes == 5:
    galoes = 0
    latas += 1
# Resultado com o menor preço
print(f'Ou, usando latas e galões juntos, para obter o menor preço', end=' ')
print(f'você precisará de {latas:.2f} latas de tinta e {galoes:.2f} galões,'
      f' que custarão, no total R${latas * 80 + galoes * 25}')
