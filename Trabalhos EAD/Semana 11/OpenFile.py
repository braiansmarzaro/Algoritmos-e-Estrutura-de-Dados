from time import sleep


def leagenda():  # atualiza a agenda
    global contatos, agenda
    '''
    Fecha e reabre o arquivo para atualizar a leitura.
    realiza a mudança de arq.readlines() para uma matriz acessível,
    separada por contatos, e cada contato com 3 informações,
    diferente de antes que seriam diversos caractéres em uma grande str
    '''
    agenda = open('Agenda.txt', 'r+')
    agenda.seek(0, 0)
    lista = agenda.readlines()  # Gera uma lista não formatada da agenda
    # Cria uma segunda lista para salvar a primeira organizada
    contatos = [''] * (len(lista))
    for i in range(len(lista)):  # Organiza as informações do arquivo em uma matriz
        contatos[i] = lista[i].split(",")[0:3]


def reticencia():
    sleep(.2)
    print(f'Retornando ao menu principal', end='')
    sleep(.5)
    print(f'.', end='')
    sleep(.5)
    print(f'.', end='')
    sleep(.5)
    print(f'.')


def add():  # Adiciona um contato à agenda

    nome = input(f'Digite o nome[25 caracteres max] ou enter para retornar ao menu: \n')
    if nome == '':  # Permite cancelar a ação caso não tenha entrada de dados
        print(f'Contato sem nome! ', reticencia())

        return  # Encerra a operação da função
    num = input(f'Digite o num[18 caracteres max] ou pressione Enter para pular:\n')
    email = input(f'Digite o email[25 caracteres max] ou pressione Enter para pular: \n')
    with open('Agenda.txt', 'a+') as mat:
        # Adiciona o novo contato ao final do arquivo, a função overwrite() organiza sua posição
        mat.write(f'{nome.title()},{num},{email}\n')
    print(f'Contato adicionado com sucesso!', reticencia())


def excluir(mat, casadeletada):  # Exclui uma linha da matriz(agenda)
    global agenda, contatos
    acao = False  # Marca se a função realizou a operação ou se foi inválida
    tamanhoIn = len(mat)  # Lê o tamanho da matriz

    # casadeletada = (input("Entre a posição a deletar: "))  # Escolhe qual linha deletar
    if casadeletada.isnumeric():
        casadeletada = int(casadeletada) - 1  # O usuário seleciona 1 para a casa 0, por exemplo, logo -1
        if (tamanhoIn > 0) and (casadeletada >= 0) and (casadeletada < tamanhoIn):
            print(f'Contato escolhido: {mat[casadeletada][0]}')

            # Exclui posição copiando as seguintes por cima, deve deixar o ultimo termo duplicado
            for i in range(casadeletada, tamanhoIn - 1):
                mat[i] = mat[i + 1]
            overwrite()  # Atualiza a agenda com o ultimo contato duplicado e o escolhido apagado
            leagenda(tamanhoIn - 1)  # Diminui uma linha na agenda
            acao = True  # Marca a realização da operação

            print(f'Contato apagado com sucesso!')
            reticencia()
        # Caso a entrada seja inválida
        else:
            print(f'Entrada inválida. ', reticencia())


def imprimematriz(mat):  # *Mostra* a matriz formatada
    for i in range(len(mat)):  # Percorre as linhas
        print(i + 1, end=' ')
        for j in range(len(mat[i])):  # Percorre cada termo da linha
            if j < len(mat[i]) - 1:  # Enquanto j n for o ultimo termo da linha
                print(f'{mat[i][j]:<25}\n')
            else:
                print(f'{mat[i][j]}')


def escrevecontato():  # Adiciona um contato ao arquivo txt
    global agenda

    nome = input(f'Digite o nome[25 caracteres max]')
    num = input(f'Digite o num[18 caracteres max]')
    email = input(f'Digite o email[25 caracteres max]')
    with open('Agenda.txt', 'a+') as agenda:
        agenda.write(f'{nome},{num},{email}\n')


def overwrite():
    global agenda
    # agenda.seek((0, 0))
    with open('Agenda.txt', 'w+') as agenda:

        for linha in contatos:
            for nome in range(len(linha)):
                if nome == len(linha) - 1:
                    agenda.write(f'{linha[nome]}')
                else:
                    agenda.write(f'{linha[nome]},')


# with open('Agenda.txt', 'r+') as agenda:  # Cria um laço de abertura do arquivo
agenda = open('Agenda.txt', 'r+')
arq = agenda.readlines()
# print(agenda) #Não funciona
agenda.seek(0, 0)  # Lê o arquivo novamente
print('agenda', arq)  # Cada linha vira uma string em uma lista
# Tentativa de ler o arquivo escrito
'''for i in range(len(arq)):
    print(agenda.readline(), end='')'''  # OK
agenda.seek(0, 0)  # reinicia a leitura do arquivo
'''for linha in agenda:

    for nome in linha:
        print(nome, end='')'''
# escrevecontato()
leagenda()
print('contatos', contatos)
overwrite()
print()

k = '\n'
print(len(k), 'k')
'''with open('Agenda.txt', 'a+') as addnofinal:
                # Adiciona o novo contato ao final do arquivo, a função overwrite() organiza sua posição depois
                addnofinal.write(f'{nome.title()},{num},{email}\n')
                addnofinal.seek(0, 0)
                tamanho = len(addnofinal.readlines())#Atualiza a leitura do tamanho do arquivo
            print(f'Tamanho é {tamanho}')

            # Exclui o contato desatualizado, função excluir(mat,casadeletada) alterada
            if tamanho > 0:
                # Exclui posição copiando as seguintes por cima, deve deixar o ultimo termo duplicado
                for i in range(troca, tamanho-2):
                    mat[i] = mat[i + 1]
                    print(i + 1, mat[i])
                    input('passa')
                input(f'Enter to continue')
                overwrite()  # Atualiza a agenda com o ultimo contato duplicado e o escolhido apagado
                input(f'Confere se o ultimo ta duplicado')
                leagenda(tamanho)
                input(f'Terminar')
                # print(f'Contato alterado com sucesso!', reticencia())'''
