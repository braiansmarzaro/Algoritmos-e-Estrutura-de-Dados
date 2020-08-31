import csv
def imprimematriz(mat):  # *Mostra* a matriz formatada
    for i in range(len(mat)):  # Percorre as linhas
        print(i + 1, end=' ')
        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j n for o ultimo termo da linha
                print(f'{mat[i][j]:<25}', end=' ')
            else:
                print(f'{mat[i][j]}')
sellperyear=[0]*11
soma = i = 0
# Para cada modelo (modelo A 2010)
with open('VendasPorAno.CSV', newline='') as csvfile:  # Soma as vendas de cada modelo
    reader = csv.reader(csvfile, delimiter=',')  # , quotechar='|')
    for row in reader:  # row desce as linhas do arquivo e gera um vetor para cada, naquele momento
        #print(f'row {row} ')
        # Para 2010
        sellperyear[i]=row
        i+=1
imprimematriz(sellperyear)