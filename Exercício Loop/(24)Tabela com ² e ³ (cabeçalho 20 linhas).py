'''Escrever um programa que lê um conjunto não determinado de valores, um de cada vez,
e escreve uma tabela com cabeçalho, que deve ser repetido a cada 20 linhas.
A tabela conterá o valor lido, seu quadrado, seu cubo e sua raiz quadrada. '''
from random import randint

r = ''
while True:
    for c in range(1, 41):
        if c % 20 == 0:
            r = str(input('Deseja continuar?[S/N]').upper().strip()[0])
        if c == 1 or c % 20 == 0:
            print('=-' * 30)
            print(f'{"           TABELA DE QUADRADOS, CUBOS E RAÍZES":^20}')
            print('=-' * 30)
        if r == 'N':
            break
        n = randint(0, 50)
        quad = n ** 2
        cube = n ** 3
        raiz = n ** .5
        print(f'{n:<5} | {quad:<5} | {cube:<5} | {raiz:<5.3f}')
