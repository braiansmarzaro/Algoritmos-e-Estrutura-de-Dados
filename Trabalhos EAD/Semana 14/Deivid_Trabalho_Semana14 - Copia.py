# Deivid Braian Smarzaro
'''Fazer um programa em Python para calcular o custo de produção, o
total de vendas e o lucro de uma montadora de automóveis no período de 2010
a 2019, em função dos seguintes dados de entrada:
VendasPorAno.CSV;“ValorMedioVendaPorAno.CSV;“ComponentesPorModelo.CSV '''
'''Calcular e imprimir o total de vendas, o custo de produção e o lucro, por modelo,
no período de 2010 a 2019. '''
#Obs: Os arquivos lidos devem estar na mesma pasta em que se encontra este programa
import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

def cabecalho():
    print(f"{'Modelo':<20} {'Vendas(2010 - 2019)':^20} {'Custo(2010 - 2019)':^28} {'Lucro(2010 - 2019)':>20}")


def geramatrizcsv(arquivo, tamanho):
    i = 0
    # Para cada modelo (modelo A 2010)
    with open(arquivo, newline='') as csvfile:  # Soma as vendas de cada modelo
        reader = csv.reader(csvfile, delimiter=',')
        matrizcsv = [0] * tamanho

        for row in reader:  # row desce as linhas do arquivo e gera um vetor para cada, naquele momento
            # print(f'row {row} ')
            # Para 2010
            matrizcsv[i] = row
            i += 1
    return matrizcsv


def geramatriz(l=7, c=4):  # Cria a matriz final vazia
    '''
    :param l: Linhas
    :param c: Colunas
    :return: A matriz gerada com 0's
    '''
    cabecalho()
    mat = [['0'] * c for z in range(l)]
    # preenche a primeira coluna para corresponder a linha do arquivo VendasPorAno

    return mat


def imprimematriz(mat):  # *Mostra* a matriz formatada
    for i in range(0, len(mat)):  # Percorre as linhas

        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j n for o ultimo termo da linha
                if j>0:
                    print(f'{locale.currency(float(mat[i][j]), grouping=True):<25}', end=' ')
                else:
                    print(f'{mat[i][j]:<20}',end=' ')
            else:
                print(locale.currency(float(mat[i][j]),grouping=True))
    count=0 #Para não dar Float de uma string
    for c in crialistatotal(): #Imprime o vetor total abaixo da matriz
        if count>0:
            print(f'{locale.currency(float(c),grouping=True):<26}', end='')
        else:
            print(f'{c:<21}',end='')
        count=1

def preenchecoluna(mat, coluna, conteudo):  # preenche as informações de cada coluna, individualmente
    '''
    :param mat: A matriz a ser preenchida
    :param coluna: Qual coluna da matriz será preenchida
    :param conteudo:
    :return:
    '''
    for linha in range(0, len(mat)):
        mat[linha][coluna] = conteudo[linha + 1]


def vendamodelo(linha):
    '''
    Realiza a somatória do valor das vendas para 1 modelo(linha) entre 2010 e 2019
    :param linha: Refere-se a linha no arquivo ValorMedioVendaPorAno.CSV
    e à coluna no arquivo VendasPorAno.CSV
    :return:
    '''
    soma = 0
    for c in range(1, len(ValorMedioVendaPorAno[linha])):
        soma += float(VendasPorAno[c][linha]) * float(ValorMedioVendaPorAno[linha][c])
    return soma


def customodeloano(linha):  # Linha refere-se a linha de Componentes por modelo e consequentemente, o modelo
    csoma = cano = 0  # Somatória das multiplicações
    for ano in range(len(CustoComponentesPorAno) - 1):  # Para cada ano
        for c in range(1, len(ComponentesPorModelo[linha])):  # Para cada coluna da linha
            cano += float(ComponentesPorModelo[linha][c]) * float(
                CustoComponentesPorAno[c][1 + ano])  # Acumula a multiplicação
        csoma += cano * float(VendasPorAno[ano + 1][linha])
        # print("csoma = ", csoma)
        cano = 0
    return csoma


def vendatotal():  # Realiza a somatória das Vendas de cada modelo, entre 2010-2019, gera o preço total
    somavenda = 0
    for i in range(1, len(ValorMedioVendaPorAno)):
        somavenda += vendamodelo(i)

    return somavenda


def custototal():
    soma = 0
    for k in range(0, len(matriz)):
        soma += customodeloano(k + 1)
    return soma


def lucrototal():
    soma = 0
    for k in range(0, len(matriz)):
        soma += float(crialistalucro()[k + 1])
    return soma


def crialistavenda():
    vet = [0] * 8
    for i in range(0, 8):
        vet[i] = f'{vendamodelo(i):.2f}'
    return vet


def crialistacusto():
    custo = [0] * 8  # A primeira casa não é utilizada
    for k in range(0, len(matriz)):
        custo[k + 1] = f'{customodeloano(k + 1):.2f}'
    return custo


def crialistatotal():
    vet = [0] * len(matriz[0])  # Cria um vetor com número de casas de uma linha da Matriz
    vet[0] = 'Total'
    vet[1] = f'{vendatotal():.2f}'
    vet[2] = f'{custototal():.2f}'
    vet[3] = f'{lucrototal():.2f}'
    return vet


def crialistalucro():
    lucro = [0] * 8  # A primeira casa não é utilizada
    for c in range(0, len(matriz)):
        lucro[c + 1] = f'{vendamodelo(c + 1) - customodeloano(c + 1):.2f}'
    return lucro


###Programa principal###

# Usa os arquivos disponíveis e gera uma matriz de cada
VendasPorAno = geramatrizcsv('VendasPorAno.CSV', 11)
ValorMedioVendaPorAno = geramatrizcsv("ValorMedioVendaPorAno.CSV", 8)
ComponentesPorModelo = geramatrizcsv("ComponentesPorModelo.CSV", 8)
CustoComponentesPorAno = geramatrizcsv("CustoComponentesPorAno.CSV", 11)

matriz = geramatriz()  # Cria a matriz final vazia
preenchecoluna(matriz, 0, VendasPorAno[0])  # Preenche a primeira coluna da matriz com os modelos
preenchecoluna(matriz, 1, crialistavenda())  # Preenche a segunda coluna com os valores de venda
preenchecoluna(matriz, 2, crialistacusto())  # Preenche a terceira coluna com os valores de custo
preenchecoluna(matriz, 3, crialistalucro())  # Preenche a ultima coluna com o lucro para cada modelo
imprimematriz(matriz)  # Mostra a matriz preenchida correntamente
