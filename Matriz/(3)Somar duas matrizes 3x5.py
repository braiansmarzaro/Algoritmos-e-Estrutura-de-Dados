'''Faça um programa que leia duas matrizes 3 X 5,
calcule e imprima a soma das duas'''
from random import randint

m = 5  # Número de colunas
n = 3  # Número de linhas
# Gera a matriz
mat = [[0] * m for i in range(n)]
for c in range(m):
    for l in range(n):
        mat[l][c] = randint(1, 10)
for i in range(len(mat)):  # Mostra a matriz
    print(mat[i])
