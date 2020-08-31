# Deivid Braian Smarzaro; Eng Metal. 2020.1

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999).
# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
#
#    Avaliação:
#    Questão 1 - Ler dados						     						 (20) : 20
#    Questão 2 - Maior e menor índice de acidentes e a que cidade pertence   (30) : 30
#    Questão 3 - Média de veículos nas cinco cidades juntas    		     	 (20) :  0 - Não calcula/escreve certo
#    Questão 4 - Média de acidentes de trânsito cidades com menos de 2.000...(30) : 30
#    Total                                                                  (100) : 80
#
#    * Execução de teste abaixo:
#

# C:\Program Files (x86)\Notepad++>"C:\Program Files (x86)\Python38-32\python.exe" "C:\IFES\AED\2020-1\Trabalhos\Trabalho_Semana4\_Correcao\Deivid_Trabalho_Semana4.py"
# Código da cidade: 1
# Quantidade de veículos na cidade em 1999: 1000
# Quantidade de acidentes com vítima em 1999: 10
# Código da cidade: 2
# Quantidade de veículos na cidade em 1999: 1500
# Quantidade de acidentes com vítima em 1999: 20
# Código da cidade: 3
# Quantidade de veículos na cidade em 1999: 2000
# Quantidade de acidentes com vítima em 1999: 30
# Código da cidade: 4
# Quantidade de veículos na cidade em 1999: 2500
# Quantidade de acidentes com vítima em 1999: 40
# Código da cidade: 5
# Quantidade de veículos na cidade em 1999: 3000
# Quantidade de acidentes com vítima em 1999: 50
# O menor índice de acidentes é 10 acidente(s), na cidade de código 1
# O maior índice de acidentes é 50 acidentes, na cidade de código 5
# A média de veículos das 5 cidades é de 30,00 veículos
# A média de acidentes nas acidentes com menos de 2000 veículos é de 15,0 acidentes,totalizando 30 acidentes entre 2 cidades contabilizadas

# C:\Program Files (x86)\Notepad++>pause
# Press any key to continue . . .


'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados: Código da cidade;
Número de veículos de passeio (em 1999); Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. '''
cidade = {}  # Dicionário para salvar cada cidade
lista = []  # Lista as cidades com suas respectivas informações
soma = soma2 = media2 = cont = 0  # Variáveis utilizadas

for c in range(0, 5):  # Lê 5 cidade
    cidade['Código: '] = str(input('Código da cidade: '))  # Código da cidade;
    # Número de veículos de passeio (em 1999);
    cidade['Veículos em 1999:'] = int(input('Quantidade de veículos na cidade em 1999: '))
    while cidade['Veículos em 1999:'] <= 0:
        print('Erro, número negativo ou 0 de veículos')
        cidade['Veículos em 1999:'] = int(input('Por favor, insira a quantidade de veículos na cidade em 1999: '))
    # Número de acidentes de trânsito com vítimas (em 1999).
    cidade['Número de acidentes com vítima em 1999: '] = int(input('Quantidade de acidentes com vítima em 1999: '))
    while cidade['Número de acidentes com vítima em 1999: '] <= 0:
        print('Erro, número negativo ou 0 de acidentes')
        cidade['Número de acidentes com vítima em 1999: '] = int(input('Por favor, insira a quantidade de acidentes '
                                                                       'com vítima em 1999: '))
    # Número de acidentes de trânsito com vítimas (em 1999).
    lista.append(cidade.copy())
    cidade.clear()

# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
menor = maior = lista[0]['Número de acidentes com vítima em 1999: ']
cidmen = cidmai = lista[0]['Código: ']  # Cidades com maior e menor índice de acidentes
for k in lista:
    soma += k['Número de acidentes com vítima em 1999: ']  # Soma os números de acidentes entre todas as cidades
    if k['Número de acidentes com vítima em 1999: '] > maior:
        maior = k['Número de acidentes com vítima em 1999: ']
        cidmai = k['Código: ']
    if k['Número de acidentes com vítima em 1999: '] < menor:
        menor = k['Número de acidentes com vítima em 1999: ']
        cidmen = k['Código: ']
    # Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
    if k['Veículos em 1999:'] < 2000:
        soma2 += k['Número de acidentes com vítima em 1999: ']
        cont += 1
        if cont==0:
            media2=0
        else:
            media2 = soma2 / cont  #Média

media = soma / 5  # Realiza a média aritmética de veículos nas 5 cidades
print(f'O menor índice de acidentes é {menor} acidente(s), na cidade de código {cidmen}\n'
      f'O maior índice de acidentes é {maior} acidentes, na cidade de código {cidmai}\n'
      f'A média de veículos das 5 cidades é de {media:.2f} veículos'.replace('.', ','))
if cont==0:
    print(f'Não há cidades com menos de 2000 veículos')
else:
    print(f'A média de acidentes nas acidentes com menos de 2000 veículos é de {media2} acidentes,'
          f'totalizando {soma2} acidentes entre {cont} cidades contabilizadas'.replace('.', ','))
