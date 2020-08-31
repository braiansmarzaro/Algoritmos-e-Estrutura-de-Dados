'''Escrever um programa para armazenar valores inteiros em uma matriz 5 x 6.
A seguir, calcular e escrever a média dos valores pares contidos
 na matriz e o seu conteúdo. '''
from random import randint
m=6 #Número de colunas
n=5 #Número de linhas
# Gera a matriz
mat = [[0] * m for i in range(n)]
for c in range(m):
    for l in range(n):
        mat[l][c] = randint(1,10)
for i in range(len(mat)):  # Mostra a matriz
    print(mat[i])
soma = cont = 0
for j in mat:
    for k in j:
        if k % 2 == 0:
            soma += k
            cont += 1
print(f'Foram contados {cont} numeros pares. Média de {soma / cont}')

