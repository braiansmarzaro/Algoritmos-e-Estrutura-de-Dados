'Lê 50 notas e mostra a média'

from random import randint
menor=maior=0
tupla=cont = 0
for c in range(0, 50):
    n = randint(0, 10)
    if n>maior:
        maior=n
    if n<menor:
        menor=n
    cont += n
media = cont / 50
print(media)
print(f'A menor nota foi {menor} e a maior nota foi {maior}')


