'''1)Ler 30 números inteiros entre 0 e 10, armazenando-os em um vetor.
Alternativamente, pode-se preencher os elementos do vetor com valores aleatórios, entre 0 e 10,
obtidos através da função randint, do módulo random.
2)Imprimir o conteúdo do vetor em uma só linha da tela, separando os elementos por uma vírgula
Vetor lido:
3)Imprimir a maior sequência não decrescente armazenada no vetor e o seu tamanho'''
from random import randint

lista = []
cresc = []
save = []
maior = 0
for c in range(30):
    n = randint(0, 10)
    lista.append(n)
print(lista)
for j in lista:
    if j >= maior:
        cresc.append(j)
        maior = j
    else:
        maior=0
        if len(save)<len(cresc):
            save.clear()
            save.append(cresc[:])
            cresc.clear()
print(save)