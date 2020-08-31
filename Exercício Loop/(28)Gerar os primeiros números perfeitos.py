'''Gerar e imprimir os 4 primeiros números perfeitos'''
from datetime import datetime
tempoInic = datetime.now()
cont = numIteracoes = 0
n=2
while cont < 4:
    n += 2
    soma = 0
    for c in range(1, n + 1):
        if n % c == 0 and n!=c:
            soma += c
        numIteracoes+=1
    if soma==n:
        print(f'O número {c} é perfeito!')
        cont+=1
tempoFim = datetime.now()
print(f"Tempo de processamento: {int((tempoFim - tempoInic).total_seconds() * 1000)} ms")
print(f"Número de iterações: {numIteracoes}")