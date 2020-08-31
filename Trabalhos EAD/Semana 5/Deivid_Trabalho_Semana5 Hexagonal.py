# Deivid Braian Smarzaro; Eng. Metal 2020.1
# Escreva um programa que gere (e imprima) os quatro primeiros números perfeitos
# da forma mais otimizada, dentro das regras.
# Número total de iterações: 4317;Tempo de processamento: 3 ms, em média.
# links utilizados: https://pt.wikipedia.org/wiki/N%C3%BAmero_perfeito;
# https://pt.wikipedia.org/wiki/Número_hexagonal .
# Os prints foram trocados por prints formatados (print(f'...'))
# Acumuladores foram trocados para o modelo x+=c (Original: x=x+c)
# A variável numTeste recebe os valores de números hexagonais, não mais conta de 1 em 1.
# A variável tempo foi deletada, seu conteúdo foi passado para o print
# Foram adicionadas as variáveis: hexa; n.
# Import datetime foi trocado para from datetime import datetime
import datetime

tempoInic = datetime.now()
contPerf = 0  # Quantos números perfeitos foram encontrados até o momento
numIteracoes = 0  # Conta a quantidade de iterações do programa
# número utilizado na variável hexa; Os números perfeitos conhecidos são hexagonais e triangulares, segundo a fonte.
k = 1
n = 2**k
numTeste = (2 * n * (2 * n - 1)) // 2  # Usa a propriedade dos números hexagonais para definir o número teste
print(f"{numTeste} é um número perfeito!")
while contPerf < 3:  # Enquanto não encontrar 4 números perfeitos
    k+=1
    n=2**k
    if k%2!=0:  # Apenas expoentes pares formam números perfeitos
        k += 1
        n = 2 ** k
    numTeste = (2 * n * ((2 * n) - 1)) // 2
    somaDiv = 3
    divisor = 3
    while divisor <= (numTeste + 1) // 2:
        if (numTeste % divisor) == 0:
            somaDiv += divisor
        divisor += 1
        numIteracoes += 1
        # print(somaDiv)
    if somaDiv == numTeste:
        print(f"{numTeste} é um número perfeito!")
        contPerf += 1

tempoFim = datetime.datetime.now()
print("Tempo de processamento:", int((tempoFim - tempoInic).total_seconds() * 1000),"ms")
print("Número de iterações:",numIteracoes)