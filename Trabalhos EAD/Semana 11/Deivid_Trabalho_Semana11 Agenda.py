# Deivid Braian Smarzaro; Eng. Metal. 2020.1
'''Criar um programa do tipo Agenda em python'''
# Informações: Coloque o arquivo txt na mesma pasta em que se encontra este arquivo. Para alterar informações para
# vazio, teclar espaço e enter. Foram feitos alguns tratamentos de exceções para evitar entradas incorretas,
# resultando na mensagem "Entrada inválida". A agenda não permite adicionar nome vazio.
# Caso o arquivo seja manipulado manualmente e ocorra de haver uma linha preenchida
# que não possua duas vírgulas, haverá erro.
from os import system
from time import sleep


def retornando():  # Função utilizada para informar a mudança de volta ao menu
    print(f'Retornando ao menu principal...')
    sleep(1.5)


def clear():  # Limpa o terminal
    system('cls')


def menu():  # Deleta o histórico e Abre um menu interativo
    clear()
    print('''
    Menu Principal
    1. Exibir agenda
    2. Adicionar item
    3. Excluir item
    4. Alterar nome, telefone ou e-mail
    S. Sair''')


def organizamatriz(mat):  # Organiza os contatos pelo primeiro termo usando bubblesort
    for j in range(0, len(mat) - 1):
        for c in range(0, len(mat) - 1):
            if mat[c] >= mat[c + 1]:
                aux = mat[c]
                mat[c] = mat[c + 1]
                mat[c + 1] = aux


def imprimematriz(mat):  # *Mostra* a matriz formatada
    clear()
    organizamatriz(mat)
    print(f'{"  Nome":<26}{"   Número":<26}{"    e-mail":<26}\n')
    for i in range(len(mat)):  # Percorre as linhas
        print(i + 1, end=' ')  # Mostra um índice para cada linha
        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j não for o ultimo termo da linha
                print(f'{mat[i][j]:<26}', end=' ')
            else:
                print(f'{mat[i][j]}')


def overwrite():  # Atualiza o arquivo agenda.txt através da matriz 'contatos', organizando-o
    global agenda
    organizamatriz(contatos)  # Organiza a matriz por ordem alphanumérica

    # Abre o arquivo para escrita e leitura
    # deletando as informações antigas para preencher com as informações da lista 'contatos'
    with open('Agenda.txt', 'w+') as agenda:

        for linha in contatos:  # Seleciona cada linha da matriz
            for nome in range(len(linha)):  # Seleciona cada informação das linhas
                if nome == len(linha) - 1:  # Para a ultima informação da linha
                    agenda.write(f'{linha[nome]}')
                else:  # Para as informações anteriores na linha imprime uma vírgula junto
                    agenda.write(f'{linha[nome]},')


def leagenda(tamanhoin):
    '''
    atualiza a matriz contatos e sincroniza a agenda. é possível diminuir tamanhoin para reduzir a agenda.
    realiza a mudança de agenda.readlines() para uma matriz acessível,
    separada por contatos(linha), e cada contato com 3 informações(cada info é uma posição de uma lista interna),
    diferente de antes, que seriam diversos caractéres em uma grande str
    :param tamanhoin: Tamanho desejado de leitura da agenda
    Retorna o arquivo organizado e sincronizado com a matriz contatos
    '''
    global contatos, agenda
    agenda.close()
    agenda = open('Agenda.txt', 'r+')
    agenda.seek(0, 0)  # Reinicia o ponto de leitura do arquivo para o início(linha 1)
    lista = agenda.readlines()  # Gera uma lista não formatada da agenda
    # (re)Cria uma segunda lista para salvar a primeira, organizando-a em grupos de 3 termos, separados por vírgula
    contatos = [''] * tamanhoin
    for i in range(0, tamanhoin):  # Organiza as informações do arquivo em uma matriz
        contatos[i] = lista[i].split(",")[0:3]
    overwrite()
    # Deleta a linha caso esteja vazia(apenas um termo não se confunde com informações em branco,
    # pois assim, ela ainda conta para o tamanho do vetor, mantendo suas vírgulas)
    while len(contatos[0]) == 1:
        excluir(contatos, '1')


def add():  # Adiciona um contato à agenda
    clear()
    nome = input(f'Digite o nome[25 caracteres max] ou pressione Enter para retornar ao menu: \n')
    if nome.strip() == '':  # Permite cancelar a ação caso não tenha entrada de dados
        print(f'Contato sem nome! ')
        retornando()
        return  # Encerra a operação da função
    num = input(f'Digite o num[18 caracteres max] ou pressione Enter para pular:\n')
    email = input(f'Digite o email[25 caracteres max] ou pressione Enter para pular: \n')
    with open('Agenda.txt', 'a') as arq:
        # Adiciona o novo contato ao final do arquivo, a função overwrite() organiza sua posição
        arq.write(f'\n{nome.title()},{num},{email}\n')
    print(f'Contato adicionado com sucesso!')
    retornando()


def excluir(mat, casadeletada):  # Exclui uma linha da matriz mat, escolhida pelo número de linha da agenda
    tamanhoIn = len(mat)  # Lê o tamanho da matriz
    if casadeletada.isnumeric():  # Valida a entrada
        casadeletada = int(casadeletada) - 1  # O usuário seleciona 1 para a casa 0, por exemplo, logo -1
        if (tamanhoIn > 0) and (casadeletada >= 0) and (casadeletada < tamanhoIn):
            # Exclui posição copiando as seguintes por cima, deve deixar o ultimo termo duplicado
            for i in range(casadeletada, tamanhoIn - 1):
                mat[i] = mat[i + 1]
            overwrite()  # Atualiza a agenda com o ultimo contato duplicado e o escolhido apagado
            leagenda(tamanhoIn - 1)  # Diminui uma linha na agenda
            return True  # Informa que a função foi utilizada corretamente
        # Caso a entrada seja inválida


def alterar(mat):
    global tamanho

    imprimematriz(mat)  # Mostra a agenda ao usuário
    troca = input(f'Qual contato deseja alterar?[Número apenas]\n').strip()  # Troca é o número do contato na lista.
    if troca.isnumeric():  # Valida a entrada da informação
        troca = int(troca) - 1  # -1 para ajustar para lista começando em 0
        if (troca >= 0) and (troca < tamanho):  # Valida a entrada da informação
            # Função add(mat) alterada
            nome = input(f'Mudar nome {mat[troca][0]} para: [Pressione enter para pular] \n')
            if nome.strip() == '':  # Caso não seja alterado, retorna ao valor original
                nome = mat[troca][0]  # Realiza a mudança da informação
            mat[troca][0] = f'{nome.title()}'
            num = input(f'Mudar número {mat[troca][1]} para: [Pressione Enter para pular] \n')
            if num == '':  # Caso não seja alterado, retorna ao valor original
                num = mat[troca][1]
            mat[troca][1] = num  # Realiza a mudança da informação
            email = input(f'Mudar e-mail {mat[troca][2]} para: [Pressione Enter para pular] \n')
            if email == '':  # Caso não seja alterado, retorna ao valor original
                email = mat[troca][2]
            mat[troca][2] = f'{email}\n'  # Realiza a mudança da informação
            print(f'Contato alterado com sucesso!')
            retornando()
            overwrite()
        else:
            print(f'Número inválido')
            retornando()
    else:
        print(f'Número inválido ou não informado. ')
        retornando()


# Programa principal

sair = False
while not sair:  # sair==False
    # Abre o arquivo para leitura e escrita ao iniciar o programa
    agenda = open('Agenda.txt', 'r+')
    tamanho = len(agenda.readlines())  # acompanha o tamanho do arquivo
    leagenda(tamanho)  # Lê o arquivo, organizando-o
    menu() #Mostra o menu interativo
    opc = input(f'Seleciona uma opção: ')
    # Valida a entrada como número ou letra dentro da lista pré-determinada
    if opc[0] in '1234Ss':
        if opc.upper().strip()[0] == 'S':  # Termina o programa
            sair = True
            agenda.close()
            print(f'Operação finalizada.\n Seu progresso foi salvo com sucesso!')

        elif opc[0] == '1':  # Mostrar agenda
            imprimematriz(contatos)
            input('\nPressione enter para voltar ao menu')
            retornando()
        elif opc[0] == '2':  # Adicionar Item
            add()
        elif opc[0] == '3':  # Excluir Item
            imprimematriz(contatos)  # Imprime a matriz para o usuário
            k = excluir(contatos, input("Entre a posição a deletar: "))
            if k:  # Caso a função ocorra corretamente
                print(f'Contato apagado com sucesso!')
            else:
                print('Entrada inválida.')
            retornando()
        elif opc[0] == '4':  # Alterar contato
            alterar(contatos)

    else:
        print(f'Entrada inválida')
        retornando()
