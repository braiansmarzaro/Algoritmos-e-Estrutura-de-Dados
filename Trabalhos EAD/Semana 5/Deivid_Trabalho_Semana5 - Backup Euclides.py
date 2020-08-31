# Deivid Braian Smarzaro; Eng. Metal 2020.1
# Escreva um programa que gere (e imprima) os quatro primeiros números perfeitos
# da forma mais otimizada, dentro das regras.
# Número total de iterações: 3;Tempo de processamento: 0 ms.
# Fonte: https://pt.wikipedia.org/wiki/N%C3%BAmero_perfeito#N%C3%BAmeros_perfeitos_pares;
# Os prints foram trocados por prints formatados (print(f'...'))
# Acumuladores foram trocados para o modelo x+=c (Original: x=x+c)
# A variável numTeste recebe os valores de números que obedecem a fórmula de euclides
# ((2 ** (n - 1)) * (2 ** n - 1)
# em que n é um número primo e ((2**n)-1) também é primo,
# logo, o resultado da fórmula é um número perfeito, de acordo com a fonte.
# A variável tempo foi deletada, seu conteúdo foi passado para o print
# Foram adicionadas as variáveis: k; n;contaprimo;cont.
# Foram deletadas as variáveis contPerf;somaDiv;
# Import datetime foi trocado para from datetime import datetime
from datetime import datetime

contaprimo = 0
tempoInic = datetime.now()
contPerf = 0  # Quantos números perfeitos foram encontrados até o momento
numIteracoes = 0  # Conta a quantidade de iterações do programa
k = 2
n = 3
# número utilizado na variável hexa; Os números perfeitos conhecidos são hexagonais e triangulares, segundo a fonte.
numTeste = (2 ** (k - 1)) * (2 ** k - 1)  # Usa a propriedade dos números euclidianos(visto fonte)
print(f"{numTeste} é um número perfeito!")
while contPerf < 3:  # Enquanto não encontrar 4 números perfeitos
    contaprimo = 0
    while contaprimo < 1:
        cont = 0  # Conta a quantidade de divisões funcionais
        divisor = 2  # Divisor
        while n / 2 > divisor:  # Enquanto o divisor for menor que a metade do número
            if n % divisor == 0:  # testa se é divisível
                cont += 1  # E acumula a quantidade de vezes que foi
            numIteracoes += 1
            divisor += 1  # aumenta o divisor
        if cont == 0:  # Se não houver nenhum divisível, é primo
            contaprimo += 1  # Conta a quantidade de primos obtidos
            numTeste = (2 ** (n - 1)) * (2 ** n - 1)
    n+=2
    print(f"{numTeste} é um número perfeito!")
    contPerf += 1
tempoFim = datetime.now()
print(f"Tempo de processamento: {int((tempoFim - tempoInic).total_seconds() * 1000)} ms")
print(f"Número de iterações: {numIteracoes}")
