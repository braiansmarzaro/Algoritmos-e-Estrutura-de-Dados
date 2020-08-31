from random import randint


def geramatriz(l=2, c=2):
    '''
    :param l: Linhas
    :param c: Colunas
    :return: A matriz gerada com 0's
    '''
    mat = [[0] * c for z in range(l)]
    return mat
def testadiagonal(mat):
    # Testa Diagonal principal
    #diagonal=False
    '''for d in range(len(velha) - 1):
        if mat[d][d] == mat[d + 1][d + 1] :#and (mat[d][d] in 'XO'):
            diagonal = True
        else:
            diagonal = False
            break'''
    #Testa contradiagonal
    for d in range(len(mat) - 1):
        if mat[d][len(mat) - 1 - d] == mat[d + 1][d-2] :#and (mat[d][d] in 'XO'):
            contradiagonal = True
        else:
            contradiagonal = False
            break
    if contradiagonal:
        return True
    else:
        return False
def testalinha(mat, linha):
    for c in range(len(mat) - 1):
        if mat[linha][c] == mat[linha][c + 1] :#and mat[linha][c] in 'XO':
            continue  # Continua o loop
        else:
            return False  # Se falhar uma vez retorna False
    return True  # Caso não falhe retorna True
def testacoluna(mat, coluna):
    for c in range(len(mat[0]) - 1):
        if mat[c][coluna] == mat[c + 1][coluna] :#and mat[c][coluna] in 'XO':
            continue  # Continua o loop
        else:
            return False  # Se falhar uma vez retorna False
    return True  # Caso não falhe retorna True
def imprimematriz(mat):  # *Mostra* a matriz formatada
    for i in range(len(mat)):  # Percorre as linhas
        print(i + 1, end=' ')
        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j n for o ultimo termo da linha
                print(f'{mat[i][j]:<25}', end=' ')
            else:
                print(f'{mat[i][j]}')

def preenchematriz(mat, r1=0, r2=50):
    '''
    :param mat: Qual matriz
    :param r1: valor minimo
    :param r2: valor máximo
    :return: a matriz preenchida
    '''
    for j in range(len(mat[0])):
        for k in range(len(mat)):
            mat[k][j] = randint(r1, r2)


def organizalinhas(mat):  # através do primeiro numero de cada sublista
    bubblesort(mat)


def organizatudo(mat):  # Organiza internamente todas as linhas da matriz *Alterar para escolher
    ''''''
    organizalinhas(mat)
    for i in range(len(mat)):
        bubblesort(mat[i])


def bubblesort(Vet):
    troca = True
    topo = len(Vet) - 2
    while troca and topo >= 0:
        troca = False
        for j in range(0, topo + 1):
            if Vet[j] > Vet[j + 1]:
                aux = Vet[j]
                Vet[j] = Vet[j + 1]
                Vet[j + 1] = aux
                troca = True
                topo = j - 1


def organizadireto(Vet):
    # Classifica o vetor em ordem crescente por Seleção Direta
    # Método otimizado
    for i in range(0, len(Vet) - 1):
        for j in range(i + 1, len(Vet)):
            if Vet[i] > Vet[j]:
                aux = Vet[i]
                Vet[i] = Vet[j]
                Vet[j] = aux


def buscabinaria(k, vet):
    '''
    :param k: O número a ser procurado
    :param vet: Em qual vetor será procurado
    :return: O numero de repetições e a casa encontrada')
    '''
    print(f'Por busca binária:')


# Teste
'''lista = geramatriz(6, 6)
preenchematriz(lista)
imprimematriz(lista)
organizalinhas(lista)
print()
print(f'Organiza linhas')
imprimematriz(lista)
print()
print(f'Organiza tudo')
organizatudo(lista)
imprimematriz(lista)'''
velha=geramatriz(3,3)
preenchematriz(velha,0,1)
print('Velha')
imprimematriz(velha)
print('Para linha')
for c in range(len(velha[0])):
    k=testalinha(velha,c)
    print(k)
print('Para coluna')
for c in range(len(velha)):
    k=testacoluna(velha,c)
    print(k)
print('Para diagonais')
k=testadiagonal(velha)
print(k)
