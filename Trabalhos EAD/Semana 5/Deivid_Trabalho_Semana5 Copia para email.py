# Deivid Braian Smarzaro; Eng. Metal 2020.1
# Escreva um programa que gere (e imprima) os quatro primeiros números perfeitos
# da forma mais otimizada, dentro das regras.
# Número total de iterações: 8658;Tempo de processamento: 2 ms, em média.
# links utilizados: https://pt.wikipedia.org/wiki/N%C3%BAmero_perfeito;
# https://pt.wikipedia.org/wiki/Número_hexagonal .
# Os prints foram trocados por prints formatados (print(f'...'))
# Acumuladores foram trocados para o modelo x+=c (Original: x=x+c)
# A variável numTeste recebe os valores de números hexagonais, não mais conta de 1 em 1.
# A variável divisor foi deletada por ser trocada pela função "for"(mudou-se de while para for, tornando-a dispensável)
# A variável tempo foi deletada, seu conteúdo foi passado para o print
# Foram adicionadas as variáveis: hexa; n.
# Import datetime foi trocado para from datetime import datetime
from datetime import datetime

tempoInic = datetime.now()
contPerf = 0  # Quantos numeros perfeitos foram encontrados até o momento
numIteracoes = 0  # Conta a quantidade de iterações do programa
# número utilizado na variável hexa; Os números perfeitos conhecidos são hexagonais e triangulares, segundo a fonte.
n = 2
numTeste = hexa = (2 * n * (2 * n - 1)) // 2  # Usa a propriedade dos números hexagonais para definir o número teste
while contPerf < 4:  # Enquanto não encontrar 4 números perfeitos
    somaDiv = 3
    for c in range(3, (numTeste + 1)//2):
        if numTeste % c == 0 and numTeste != c:
            somaDiv += c
        numIteracoes += 1
    if somaDiv == numTeste:
        print(f"{numTeste} é um número perfeito!")
        contPerf += 1
    n *= 2
    if n == 2 ** 3 or n == 2 ** 5:
        n *= 2
    numTeste = hexa = (2 * n * (2 * n - 1)) // 2
tempoFim = datetime.now()
print(f"Tempo de processamento: {int((tempoFim - tempoInic).total_seconds() * 1000)} ms")
print(f"Número de iterações: {numIteracoes}")
