# Trabalho semana 11
# On 08/16/2020
#
import os
import io
import glob
import subprocess

# Constantes
# Tamanho Máximo da Agenda
TAMMAXAGENDA = 20


# define our clear function 
def clear():
    # for windows 
    if os.name == 'nt':
        _ = os.system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

    # Le agenda do arquivo em disco


def LeAgenda(agenda, nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    tamAgenda = 0
    for linha in arquivo:
        linha = linha.rstrip('\n')  # Remoe salto de linha
        agenda[tamAgenda][0] = linha.split(",")[0]  # Popula colunas
        agenda[tamAgenda][1] = linha.split(",")[1]
        agenda[tamAgenda][2] = linha.split(",")[2]
        tamAgenda = tamAgenda + 1
    arquivo.close()
    return tamAgenda


# Grava agenda no arquivo em disco
def GravaAgenda(agenda, tamAgenda, nomeArquivo):
    arquivo = open(nomeArquivo, "w", encoding="utf-8")
    for i in range(0, tamAgenda):
        arquivo.write("%s,%s,%s\n" % (agenda[i][0], agenda[i][1], agenda[i][2]))
    arquivo.close()
    return tamAgenda


# Imprime Menu
def ImprimeMenu():
    resposta = "X"
    while resposta not in ("1", "2", "3", "4", "5", "s", "S"):
        clear()
        print("Programa Agenda")
        print("1. Exibir agenda")
        print("2. Adicionar item")
        print("3. Excluir item")
        print("4. Alterar nome, telefone ou e-mail")
        print("S. Sair")
        resposta = input("Selecione uma das opções acima: ")
    return resposta


# Imprime Agenda
def ExibeAgenda(agenda, tamAgenda):
    clear()
    print()
    print("%5s|%-25s| %-18s| %-25s" % ("Item", "Nome", "Telefone", "e-mail"))
    print("-" * 74)
    for i in range(0, tamAgenda):
        print("%5d|%-25s| %-18s| %-25s" % ((i + 1, agenda[i][0], agenda[i][1], agenda[i][2])))
    resposta = input("Tecle Enter para retornar...")


# Imprime Agenda numerada
def ExibeAgendaNumerada(agenda, tamAgenda, texto):
    numItem = -1
    while not (numItem >= 0 and numItem <= TAMMAXAGENDA):
        clear()
        print()
        print("%5s|%-25s| %-18s| %-25s" % ("Item", "Nome", "Telefone", "e-mail"))
        print("-" * 74)
        for i in range(0, tamAgenda):
            print("%5d|%-25s| %-18s| %-25s" % (i + 1, agenda[i][0], agenda[i][1], agenda[i][2]))
        try:
            numItem = int(input("%s ou 0 para sair:" % texto))
        except:
            numItem = -1
    return numItem


# Lê um item da agenda
def LeItemAgenda(texto, tamanhoMax):
    item = " " * (tamanhoMax + 1)
    while len(item) > tamanhoMax:
        item = input("Entre o %s com até %d caracteres:" % (texto, tamanhoMax))
        if len(item) > tamanhoMax:
            print("%s muito longo! Entre novamente!" % (texto))
    return (item)


# Altera um item da agenda
def AlteraCampoAgenda(texto, tamanhoMax, item):
    novoitem = " " * (tamanhoMax + 1)
    while len(novoitem) > tamanhoMax:
        novoitem = input("%s: '%s'. Novo %s com até %d caracteres:" % (texto, item, texto, tamanhoMax))
        if len(novoitem) > tamanhoMax:
            print("%s muito longo! Entre novamente!" % (texto))
        elif len(novoitem) > 0:
            item = novoitem
    return item


# Pesquisa nome na agenda
def PesquisaItemAgenda(agenda, tamAgenda, nome):
    # Pesquisar o elemento nome no vetor agenda 
    k = -1  # significa que elem ainda não foi encontrado em V
    i = 0  # índice dos elementos do vetor V
    while (i < tamAgenda) and (k == -1):
        if (agenda[i][0] == nome):
            k = i
        elif (agenda[i][0] < nome):
            i = i + 1
        else:
            k = -2;  # significa que Elem não está em V
    return i


# Insere item na agenda em uma dada posicao
def InsereItemAgenda(agenda, tamAgenda, posicAInserir, nome, telefone, email):
    # Insere elemento no vetor
    if (tamAgenda < len(agenda)) and (posicAInserir >= 0) and (posicAInserir <= tamAgenda):
        tamAgenda = tamAgenda + 1
        for i in range(tamAgenda - 1, posicAInserir, -1):
            agenda[i][0] = agenda[i - 1][0]
            agenda[i][1] = agenda[i - 1][1]
            agenda[i][2] = agenda[i - 1][2]

        agenda[posicAInserir][0] = nome
        agenda[posicAInserir][1] = telefone
        agenda[posicAInserir][2] = email
    return (tamAgenda)


# Insere item na Agenda
def AdicionaItemAgenda(agenda, tamAgenda):
    clear()
    print("Adicionar item a agenda")
    if tamAgenda == TAMMAXAGENDA:
        print("Agenda cheia!!!")
    else:
        # Lê dados
        nome = LeItemAgenda("Nome", 25)
        telefone = LeItemAgenda("Telefone", 18)
        email = LeItemAgenda("e-mail", 25)

        # Procura posição de inserção na agenda
        posicAInserir = PesquisaItemAgenda(agenda, tamAgenda, nome)

        # Insere item na agenda
        tamAgenda = InsereItemAgenda(agenda, tamAgenda, posicAInserir, nome, telefone, email)

        # Da mensagem e sai
        print("Item inserido com sucesso!")

    resposta = input("Tecle Enter para retornar...")

    # Retorna novo tamanho da agenda
    return (tamAgenda)


# Remove item da agenda
def RemoveItemAgenda(agenda, tamAgenda, posicADeletar):
    if (tamAgenda > 0) and (posicADeletar >= 0) and (posicADeletar < tamAgenda):
        for i in range(posicADeletar, tamAgenda - 1):
            agenda[i][0] = agenda[i + 1][0]
            agenda[i][1] = agenda[i + 1][1]
            agenda[i][2] = agenda[i + 1][2]

        tamAgenda = tamAgenda - 1
        return (tamAgenda)


# Insere item na Agenda
def ExcluiItemAgenda(agenda, tamAgenda):
    clear()
    print("Excluir item da agenda")

    if tamAgenda == 0:
        print("Agenda vazia!!!")
    else:
        # Solicita item a excluir
        itemAExcluir = ExibeAgendaNumerada(agenda, tamAgenda, "Selecione um item a excluir ")

        # Se foi selecionado um item valido
        if itemAExcluir != 0 and itemAExcluir <= tamAgenda:
            tamAgenda = RemoveItemAgenda(agenda, tamAgenda, itemAExcluir - 1)
            print("Item excluido com sucesso!!!")
            resposta = input("Tecle Enter para retornar...")

    # Retorna novo tamanho da agenda
    return (tamAgenda)


def AlteraItemAgenda(agenda, tamAgenda):
    clear()
    print("Alterar item da agenda")

    if tamAgenda == 0:
        print("Agenda vazia!!!")
    else:
        # Solicita item a alterar
        itemAAlterar = ExibeAgendaNumerada(agenda, tamAgenda, "Selecione um item a alterar")

        # Se foi selecionado um item valido
        if itemAAlterar != 0 and itemAAlterar <= tamAgenda:
            # Altera dados
            print("Altere os campos a seguir ou tecle Enter para deixá-los inalterados:")

            nome = AlteraCampoAgenda("Nome", 25, agenda[itemAAlterar - 1][0])
            telefone = AlteraCampoAgenda("Telefone", 18, agenda[itemAAlterar - 1][1])
            email = AlteraCampoAgenda("e-mail", 25, agenda[itemAAlterar - 1][2])

            # Exclui item atual 
            tamAgenda = RemoveItemAgenda(agenda, tamAgenda, itemAAlterar - 1)

            # Procura posição de inserção na agenda do item alterado
            posicAInserir = PesquisaItemAgenda(agenda, tamAgenda, nome)
            tamAgenda = InsereItemAgenda(agenda, tamAgenda, posicAInserir, nome, telefone, email)

            # Da mensagem e sai
            print("Item alterado com sucesso!")

    resposta = input("Tecle Enter para retornar...")


##################  Programa principal ################################################    
# Cria agenda e variável para controlar o seu tamanho
agenda = [["", "", ""] for i in range(TAMMAXAGENDA)]
tamAgenda = 0

# Le a agenda do arquivo
tamAgenda = LeAgenda(agenda, "Agenda.txt")

# Imprime Menu
resposta = "X"
while resposta.upper() != "S":
    resposta = ImprimeMenu()
    if resposta == "1":
        ExibeAgenda(agenda, tamAgenda)
    elif resposta == "2":
        tamAgenda = AdicionaItemAgenda(agenda, tamAgenda)
    elif resposta == "3":
        tamAgenda = ExcluiItemAgenda(agenda, tamAgenda)
    elif resposta == "4":
        AlteraItemAgenda(agenda, tamAgenda)

# Escreve a agenda no arquivo
tamAgenda = GravaAgenda(agenda, tamAgenda, "Agenda.txt")
