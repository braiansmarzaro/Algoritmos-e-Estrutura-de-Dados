"""Conta a quantidade de votos de 4 candidatos, votos brancos e nulos(randint)"""
from random import randint

v1 = v2 = v3 = v4 = v5 = v6 = 0
for c in range(0, 50):
    voto = randint(1, 6)
    if voto == 1:
        v1 += 1
    if 2 == voto:
        v2 += 1
    if voto == 3:
        v3 += 1
    if voto == 4:
        v4 += 1
    if voto == 5:
        v5 += 1
    if voto == 6:
        v6 += 1
print("A contagem de votos foi: ")
print(f'Candidato 1: {v1}')
print(f'Candidato 2: {v2}')
print(f'Candidato 3: {v3}')
print(f'Candidato 4: {v4}')
print(f'Votos Brancos: {v5}')
print(f'Votos nulos : {v6}')
