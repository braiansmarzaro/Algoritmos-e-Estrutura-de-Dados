'''Faça um programa que crie uma matriz 7 X 7 de inteiros, preenchendo cada
posição com 0 ou 1, e a seguir escrevendo somente a matriz triangular inferior,
conforme figura abaixo. Uma matriz triangular inferior é aquela em que os
elementos acima da diagonal principal são nulos: '''
from random import randint

# Gera a matriz
mat = [[0] * 7 for i in range(7)]
for c in range(7):
    for l in range(7):
        if l<=c:
            mat[c][l] = randint(1, 2)  # Gera a matriz aleatoriamente
for i in range(7):  # Mostra a matriz
    print()
    for j in range(7):
        if mat[i][j]!=0:
            print(mat[i][j],end=',')

