import csv
soma=0
with open('VendasPorAno.CSV', newline='') as csvfile: #Soma as vendas de cada modelo
    spamreader = csv.reader(csvfile, delimiter=',')  # , quotechar='|')
    for row in spamreader: #row desce as linhas do arquivo e gera um vetor para cada, naquele momento
        print(f'row {row} ')
        for c in range(1,len(row)):
            if row[c].isnumeric(): #Soma apenas numeros

                soma+=int(row[c])
        print(soma)
        soma=0

        with open('ValorMedioVendaPorAno.CSV', newline='') as csvfile:  # Soma as vendas de cada modelo
            valormedio = csv.reader(csvfile, delimiter=',')