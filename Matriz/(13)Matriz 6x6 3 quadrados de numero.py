'''Faça um programa para gerar a matriz 6x6 abaixo, e depois escrever o seu
conteúdo:
1 1 1 1 1 1
1 2 2 2 2 1
1 2 3 3 2 1
1 2 3 3 2 1
1 2 2 2 2 1
1 1 1 1 1 1 '''
# Gera a matriz
mat = [[0] * 6 for i in range(6)]
for c in range(6):
    for l in range(6):

        if 3 >= l >= 2 and 3 >= c >= 2:
            mat[l][c] = 3
        elif 4>= l >=1 and 4>= c >=1:
            mat[l][c] = 2
        else:
            mat[l][c] = 1

for i in range(len(mat)):  # Mostra a matriz
    print(mat[i])
