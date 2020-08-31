# Tarefa da semana Semana: 9 Nota máxima: 100 Total de pontos: 10 Descrição: Faça um programa em Python para: 1.  Ler
# dois valores inteiros m e n, entre 1 e 20. Criar um vetor de nome Vet1 de tamanho m e um vetor de nome Vet2 de
# tamanho n. Os dois vetores deverão conter valores inteiros. 2.  Preencher o vetor Vet1 com valores inteiros
# aleatórios entre 100 e 120 e o vetor Vet2 com valores inteiros aleatórios entre 150 e 170. 3.  Imprimir os vetores
# Vet1 e Vet2, conforme layout do exemplo abaixo. Para tanto, crie uma função (def), de nome ImprimeVetor,
# que receba um vetor a ser impresso e um texto a ser impresso antes do conteúdo do vetor. Os valores dos elementos
# do vetor a serem impressos deverão estar separados por virgulas. Faça uma chamada à função para imprimir Vet1 e
# outra chamada para imprimir Vet2. 4.  Criar um vetor de nome Soma, de tamanho m, se m ≥ n, ou n, se n > m. 5.
# Preencher o vetor Soma de tal forma que cada elemento i do mesmo contenha a soma dos elementos das i-ésimas
# posições de Vet1 e Vet2, se existirem, ou 0 se não existirem. Ou seja, Soma[i] = Vet1[i] + Vet2[i]. 6.  Imprimir o
# vetor Soma, conforme layout do exemplo abaixo, utilizando a função ImprimeVetor, criada no item 3. 7.  Calcular e
# imprimir a soma e a média aritmética simples dos valores armazenados no vetor Soma. 8.  Calcular e imprimir a
# variância populacional  e o desvio padrão populacional  dos valores armazenados no vetor Soma. 9.  Calcular e
# imprimir a média harmônica  dos valores armazenados no vetor Soma. 10. Calcular e imprimir a média ponderada  dos
# valores armazenados em Soma, de acordo com o seguinte critério, para cada i-ésimo valor armazenado no vetor: a.  Se
# Soma[i] contiver a soma de Vet1[i] + Vet2[i], o peso da posição será 3. b.  Se Soma[i] contiver somente o valor
# oriundo de Vet1[i], o peso da posição será 2. c.  Se Soma[i] contiver somente o valor oriundo de Vet2[i],
# o peso da posição será 1. 11. Imprimir o conteúdo do vetor Soma em ordem crescente, conforme layout do exemplo
# abaixo, utilizando a função ImprimeVetor, criada no item 3. 12. Calcular e imprimir a frequência absoluta e
# relativa  dos valores armazenados no vetor Soma.


import random


def ImprimeVetor(nomeVet, Vet):
    print(nomeVet, end="")
    print("%4d" % Vet[0], end="")
    for dd in range(1, len(Vet)):
        print(",", "%4d" % Vet[dd], end="")
    print()


# Classifica o vetor em ordem crescente  por Classificacao da Bolha
def OrdenaVetor(Vet):
    for b in range(1, len(Vet)):
        for j in range(0, len(Vet) - b):
            if Vet[j] > Vet[j + 1]:
                aux = Vet[j]
                Vet[j] = Vet[j + 1]
                Vet[j + 1] = aux


###########################################################################################
print("Tarefa da semana 9")

# 1.  Ler dois valores inteiros m e n. Criar um vetor de nome Vet1 de tamanho m e um vetor de nome Vet2 de tamanho n.
# Os dois vetores deverão conter valores inteiros.
m = int(input("Entre um valor inteiro m, entre 1 e 20: "))
n = int(input("Entre um valor inteiro n, entre 1 e 20: "))
Vet1 = [0] * m
Vet2 = [0] * n

# 2.  Preencher o vetor Vet1 com valores inteiros aleatórios entre 100 e 120 e o vetor Vet2 com valores inteiros
# aleatórios entre 150 e 170.
for i in range(0, len(Vet1)):
    Vet1[i] = random.randint(100, 120)
for i in range(0, len(Vet2)):
    Vet2[i] = random.randint(150, 170)

# 3.  Imprimir os vetores Vet1 e Vet2, conforme layout do exemplo abaixo. Para tanto, crie uma função (def),
# de nome ImprimeVetor, que receba um vetor a ser impresso e um texto a ser impresso antes do conteúdo do vetor. Os
# valores dos elementos do vetor a serem impressos deverão estar separados por virgulas. Faça uma chamada à função
# para imprimir Vet1 e outra chamada para imprimir Vet2.
ImprimeVetor("Vet1 :", Vet1)
ImprimeVetor("Vet2 :", Vet2)

# 4.  Criar um vetor de nome Soma, de tamanho m, se m ≥ n, ou n, se n > m.
if m >= n:
    Soma = [0] * m
else:
    Soma = [0] * n

# 5.  Preencher o vetor Soma de tal forma que cada elemento i do mesmo contenha a soma dos elementos das i-ésimas
# posições de Vet1 e Vet2, se existirem, ou 0 se não existirem. Ou seja, Soma[i] = Vet1[i] + Vet2[i].
Peso = [0] * len(Soma)  # Determina os pesos para o cálculo a média ponderada
somaPesos = 0  # Determina a soma dos pesos para o cálculo a média ponderada
for i in range(0, len(Soma)):
    if i <= (m - 1) and i <= (n - 1):
        Soma[i] = Vet1[i] + Vet2[i]
        Peso[i] = 3
    elif i <= (m - 1):
        Soma[i] = Vet1[i]
        Peso[i] = 2
    else:
        Soma[i] = Vet2[i]
        Peso[i] = 1
    somaPesos = somaPesos + Peso[i]

# 6.  Imprimir o vetor Soma.
ImprimeVetor("Soma :", Soma)

# 7.  Calcular e imprimir a soma e a média aritmética simples dos valores armazenados no vetor Soma.
soma = 0
for i in range(0, len(Soma)):
    soma = soma + Soma[i]
media = soma / len(Soma)
print("Soma dos valores: ", soma, "Média aritmética simples: ", "%6.2f" % media)

# 8.  Calcular e imprimir a variância populacional e o desvio padrão populacional dos valores armazenados no vetor
# Soma.
somaQuad = 0
for i in range(0, len(Soma)):
    somaQuad = somaQuad + (Soma[i] - media) ** 2
variancia = somaQuad / len(Soma)
desvioPadrao = variancia ** 0.5
print("Variância populacional: ", "%6.2f" % variancia, "Desvio padrão populacional: ", "%6.2f" % desvioPadrao)

# 9.  Calcular e imprimir a média harmônica*** dos valores armazenados no vetor Soma.
SomaInv = 0
for i in range(0, len(Soma)):
    SomaInv = SomaInv + (1 / Soma[i])
mediaHarmonica = len(Soma) / SomaInv
print("Média harmônica: ", "%6.2f" % mediaHarmonica)

# 10. Calcular e imprimir a média ponderada  dos valores armazenados em Soma, de acordo com o seguinte critério,
# para cada i-ésimo valor armazenado no vetor: a.  Se Soma[i] contiver a soma de Vet1[i] + Vet2[i], o peso da posição
# será 3. b.  Se Soma[i] contiver somente o valor oriundo de Vet1[i], o peso da posição será 2. c.  Se Soma[i]
# contiver somente o valor oriundo de Vet2[i], o peso da posição será 1.
soma = 0
for i in range(0, len(Soma)):
    soma = soma + (Soma[i] * Peso[i])
print("Média ponderada: ", "%6.2f" % (soma / somaPesos))

# 11. Imprimir o conteúdo do vetor Soma em ordem crescente, conforme layout do exemplo abaixo, utilizando a função
# ImprimeVetor, criada no item 3.
OrdenaVetor(Soma)
ImprimeVetor("Soma em ordem crescente:", Soma)

# 12. Calcular e imprimir a frequência absoluta e relativa  dos valores armazenados no vetor Soma.
ContRep = 1
for i in range(1, len(Soma)):
    if Soma[i] != Soma[i - 1]:
        print("Valor = ", "%4d" % (Soma[i - 1]), " Frequencia abs. = ", "%4d" % ContRep, " Frequencia rel. = ",
              "%6.4f" % (ContRep / len(Soma)))
        ContRep = 1
    else:
        ContRep = ContRep + 1
print("Valor = ", "%4d" % (Soma[len(Soma) - 1]), " Frequencia abs. = ", "%4d" % ContRep, " Frequencia rel. = ",
      "%6.4f" % (ContRep / len(Soma)))
