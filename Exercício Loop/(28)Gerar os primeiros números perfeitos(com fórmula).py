# fórmula de Euclides para números perfeitos 2**(n−1)*(2n−1)
from datetime import datetime
tempoInic = datetime.now()
n = 2
interacoes=0
euclides = 2 ** (n-1)* ((2**n) - 1)
print(f'{euclides} é um número perfeito!')
n=3
for c in range (0,3):
    euclides=(2 ** (n-1))* ((2**n) - 1)
    print(f'{euclides} é um número perfeito!')
    n+=2
    interacoes+=1
tempoFim = datetime.now()
print(f"Tempo de processamento: {int((tempoFim - tempoInic).total_seconds() * 1000)} ms")
print(f"Número de iterações: {interacoes}")