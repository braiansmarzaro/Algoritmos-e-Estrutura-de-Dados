'''Matriz 5x5:
a) A soma da linha 4 de M.
b) A soma da da coluna 2 de M.
c) A soma da da diagonal principal.
d) A soma da da diagonal secundária.
e) A soma da de todos os elementos da matriz.
Imprima estas somas e a matriz. '''
from random import randint

# Gera a matriz
mat = [[0] * 5 for i in range(5)]
for c in range(5):
    for l in range(5):
        mat[c][l] = randint(0, 5)  # Gera a matriz aleatoriamente
for i in range(5):  # Mostra a matriz
    print(mat[i])
# a)
soma = 0
for j in mat[3]:
    soma += j
print(f'A soma da linha 4 é {soma}')
# b)
somacol2=0
for j in range(5):
    somacol2+=mat[j][1]
print(f'A soma da coluna 2 é {somacol2}')
# c)
somadig=0
for c in range(5):
    somadig+=mat[c][c]
print(f'A soma da diagonal principal é {somadig}')
#d)
somadig2=0
for c in range(5):
    somadig2+=mat[c][4-c]
print(f'A soma da diagonal secundaria é {somadig2}')
#e)
somaall=0
for c in mat:
    for k in c:
        somaall+=k
print(f'A soma de todos os elementos é {somaall}')



