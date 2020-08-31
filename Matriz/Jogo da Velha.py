'''Criar um programa para jogar Jogo da velha usando matrizes'''
from os import system
from random import choice
from time import sleep


def clear():  # Limpa o terminal
    system('cls')


def imprimematriz(mat):  # *Mostra* a matriz formatada
    clear()
    for k in range(len(mat)):
        print(f'{k:^11}', end='')  # Mostra o índice pra cada coluna
    print()
    for i in range(len(mat)):  # Percorre as linhas
        if i > 0:
            print('  ', '-' * 30)  # printa um quebra linha
        print(i, end=' ')  # Mostra um índice para cada linha

        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j não for o ultimo termo da linha
                print(f'{mat[i][j]:^8}', end=' | ')
            else:
                print(f'{mat[i][j]:^8}')


def geramatriz(l=3, c=3):
    '''
    :param l: Linhas
    :param c: Colunas
    :return: A matriz gerada
    '''
    # mat = [[' ', 'O', 'O'],
    #      ['X', 'O', 'O'],
    #     [' ', 'X', 'X']]
    mat = []
    for z in range(l):
        mat.append([' '] * c)
    return mat


def jogada(jogador):
    global casas, casa
    while True:
        try:
            if jogador == nomedoponente(): #Caso seja o oponente a jogar
                if nomedoponente() == 'Blitzcrank':
                    casa = bot2()
                if nomedoponente() == 'Jogador 2':
                    casa = input(f'Casa [Linha e coluna][00]:').strip()
            else:
                casa = input(f'Casa [Linha e coluna][00]:').strip()
            linha = int(casa[0])
            coluna = int(casa[1])
            if velha[linha][coluna] in "XO":
                imprimematriz(velha)
                print('Casa ocupada! Tente outra casa')
                print(f'Vez do {jogador}')
                continue
            if len(casa) != 2:
                imprimematriz(velha)
                print(f'Por favor, utilize apenas dois números válidos')
                print(f'Vez do {jogador}')
                continue
        except Exception as erro:
            print(f'Erro é {erro}')
            imprimematriz(velha)
            print(f'Por favor, utilize apenas dois números válidos')
            print(f'Vez do {jogador}')
            continue
        else:
            # Saída
            casa = f'{casa}'
            print(casas)
            casas.remove(casa)
            if jogador == 'Player 1':
                velha[linha][coluna] = 'X'
            else:
                velha[linha][coluna] = 'O'
            break


def testalinha(mat, linha):
    for c in range(len(mat) - 1):
        if mat[linha][c] == mat[linha][c + 1] and mat[linha][c] in 'XO':
            continue  # Continua o loop
        else:
            return False  # Se falhar uma vez retorna False
    return True  # Caso não falhe retorna True


def testacoluna(mat, coluna):
    for c in range(len(mat[0]) - 1):
        if mat[c][coluna] == mat[c + 1][coluna] and mat[c][coluna] in 'XO':
            continue  # Continua o loop
        else:
            return False  # Se falhar uma vez retorna False
    return True  # Caso não falhe retorna True


def testadiagonal(mat):
    # Testa Diagonal principal
    # diagonal=False
    for d in range(len(mat) - 1):
        if mat[d][d] == mat[d + 1][d + 1] and (mat[d][d] in 'XO'):
            diagonal = True
        else:
            diagonal = False
            break
    # Testa contradiagonal
    for d in range(len(mat) - 1):
        if mat[d][len(mat) - 1 - d] == mat[d + 1][len(mat) - 2 - d] and (mat[d][len(mat) - 1 - d] in 'XO'):
            contradiagonal = True
        else:
            contradiagonal = False
            break
    if diagonal or contradiagonal:
        return True
    else:
        return False


def win():
    # Testas as duas diagonais
    if testadiagonal(velha):
        return True
    # Testa cada linha
    for L in range(len(velha)):
        if testalinha(velha, L):
            return True
    # Testa cada coluna
    for c in range(len(velha[0])):
        if testacoluna(velha, c):
            return True


def empate():  # avalia se todas as casas foram preenchidas
    global draw
    for c in velha:
        for k in c:
            if k == ' ':
                return False
    draw += 1
    return True


def again():
    global velha
    print(f'Deseja jogar novamente?[S/N]')
    resp = input().upper()[0]
    if resp.upper() == 'S':
        velha = geramatriz()
        casapossivel()
        imprimematriz(velha)
        print(f'Jogador 1 joga com X. {nomedoponente()} joga com O')
    else:
        para = True
        return para


def bot2():
    choose = choice(casas)
    print('Pensando...')
    sleep(1.5)

    return choose


def bot3():
    pass


def casapossivel():  # Reinicia a lista de casas possíveis de jogar
    global casas
    casas = []  # Gera as casas possíveis para lance das máquinas
    for c in range(3):
        num1 = f'{c}'
        for k in range(3):
            num2 = f'{k}'
            casas.append(num1 + num2)


def nomedoponente():  # Nomeia o oponente
    nome=''
    if oponente == 1:
        nome = 'Jogador 2'
    elif oponente == 2:
        nome = 'Blitzcrank'
    elif oponente == 3:
        nome = 'Blitz Chefão'
    return nome

# Programa principal
while True:
    try:
        print(f'''Qual será seu oponente? 
        1 para pessoa
        2 para bot iniciante
        3 para bot intermediário''')
        oponente = int(input('1,2 ou 3: '))
        if 0 < oponente > 3:
            print(a)  # Invoca um erro
    except:
        clear()
        print('Opção inválida')
        continue
    else:

        break
win1 = win2 = draw = 0
# Gera a matriz formatada
velha = geramatriz()
imprimematriz(velha)
print(f'Jogador 1 joga com X. {nomedoponente()} joga com O')
casapossivel()
while True:
    para = False
    print(f'Vez do Jogador 1')
    jogada('Player 1')
    imprimematriz(velha)
    if win():
        win1 += 1
        print(f'Jogador 1 venceu!')
        if again():
            break
    if empate():
        print('Empate!')
        if again():
            break

    print(f'Vez do {nomedoponente()}')
    jogada(nomedoponente())
    imprimematriz(velha)
    if win():
        print(f'{nomedoponente()} venceu!')
        win2 += 1
        if again():
            break
    if empate():
        print('Empate!')
        if again():
            break
clear()
print('Bom jogo!')
print(f'''Estatísticas:
Jogador 1 venceu {win1} vez(es)
{nomedoponente()} venceu {win2} vez(es)
Ocorreu(ram) {draw} empate(s)!''')
