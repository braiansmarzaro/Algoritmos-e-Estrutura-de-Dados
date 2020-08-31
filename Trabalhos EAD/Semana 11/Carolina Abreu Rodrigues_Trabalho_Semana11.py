from os import system


def exibir(myAgenda, tamAtual):
    global arq
    cont = 1
    print('myagenda',myAgenda)
    for linha in myAgenda:
        print(cont, "-", linha, "\n")
        if cont == tamAtual:
           break
        input('Enter')
        cont += 1


def adicionar(myAgenda, tamAtual):
    if tamAtual < 20:
        nome = input("Digite o nome do contato com até 25 caracteres: ")
        tel = input("Digite o telefone do contato com até 18 caracteres: ")
        email = input("Digite o e-mail do contato com até 25 caracteres: ")
        myAgenda[tamAtual - 1] = (nome, tel, email)
        exibir(myAgenda, tamAtual)
        tamAtual += 1
    else:
        print("Agenda cheia")


def excluir(myAgenda, tamAtual):
    pass


def alterar(myAgenda):
    pass


def sair():
    system("cls")


def principal():
    global arq
    arq = open("Agenda.txt", "r")
    tamMax = len(arq.readlines())
    print('tammax é,',tamMax)
    tamAtual = 0
    cont = 0
    myAgenda = [""] * tamMax


    for linha in arq:
        myAgenda[cont] = (linha.split(","))
        cont += 1

    arq.close()

    while True:
        print("1 - Exibir agenda")
        print("2 - Adicionar item")
        print("3 - Excluir item")
        print("4 - Alterar nome, telefone ou e-mail")
        print("S - Sair")
        opcao = input("Selecione uma das opções acima: ")
        print()

        if opcao == "1":
            exibir(myAgenda, tamAtual)
        elif opcao == "2":
            adicionar(myAgenda, tamAtual)
        elif opcao == "3":
            excluir(myAgenda, tamAtual)
        elif opcao == "4":
            alterar(myAgenda)
        elif opcao == "S" or "s":
            sair()
        else:
            print("Opção inválida. Por favor, tente novamente.")
        print()


principal()
