# Deivid Braian Smarzaro; Eng. Metal 2020.1
# Escreva um programa que gere (e imprima) os quatro primeiros números perfeitos
# da forma mais otimizada, dentro das regras.
# Número total de iterações: 75;Tempo de processamento: 0 ms.
# Fonte: https://pt.wikipedia.org/wiki/N%C3%BAmero_perfeito#N%C3%BAmeros_perfeitos_pares;
# https://pt.wikipedia.org/wiki/Primo_de_Mersenne.
# Os prints foram trocados por prints formatados (print(f'...'))
# Acumuladores foram trocados para o modelo x+=c (Original: x=x+c)
# A variável numTeste recebe os valores de números que obedecem a fórmula de euclides
# ((2 ** (n - 1)) * (2 ** n - 1)
# em que n é um número primo e ((2**n)-1) também é primo,
# logo, o resultado da fórmula é um número perfeito, de acordo com a fonte.
# A variável tempo foi deletada, seu conteúdo foi passado para o print
# Foram adicionadas as variáveis: k;contaprimo;cont.
# Foi deletada as variável somaDiv;
# Import datetime foi trocado para from datetime import datetime
# Obs: 'Número testado para Mersenne' significa que não se sabe se o número obedece as regras para
# ser classificado como de Mersenne, e consequentemente usado para gerar números perfeitos
from datetime import datetime

contaprimo = 0
tempoInic = datetime.now()
contPerf = 0  # Quantos números perfeitos foram encontrados até o momento
numIteracoes = 0  # Conta a quantidade de iterações do programa
k = 2  # Variável inicial utilizada nos números de Mersenne, que são, por sua vez, utlizados na fórmula de Euclides
numTeste = (2 ** (k - 1)) * (2 ** k - 1)  # Usa a propriedade dos números euclidianos(visto fonte)
print(f'{k} é um número primo e {numTeste} é um número perfeito!')
k += 1
while contPerf < 5:  # Enquanto não encontrar 4 números perfeitos
    contaprimo = 0
    while contaprimo < 1:  # Gera números primos compatíveis com os números de Mersenne
        cont = 0  # Conta a quantidade de divisões funcionais
        divisor = 2  # Divisor
        while (2 ** k) - 1 > divisor and cont == 0:  # Enquanto o divisor for menor que a metade do número
            # testado para número de Mersenne e se manter verdade
            numIteracoes += 1
            if ((2 ** k) - 1) % divisor == 0:  # Acusa o número testado para Mersenne de não ser primo
                cont += 1
            divisor += 1
        if cont == 0:
            numTeste = (2 ** (k - 1)) * (2 ** k - 1)
            print(f'{k} é um número primo e {numTeste} é um número perfeito!')
            contPerf += 1
        k += 2
        contaprimo += 1  # Conta a quantidade de primos obtidos

tempoFim = datetime.now()
print(f"Tempo de processamento: {int((tempoFim - tempoInic).total_seconds() * 1000)} ms")
print(f"Número de iterações: {numIteracoes}")
