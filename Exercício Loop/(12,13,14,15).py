"""Ler x valores inteiros. Mostrar o Maior e o menor dentre eles.
 Mostrar quantos estão entre 0-25,26-50,51-75,76-100. Finalizar com número negativo"""
maior = menor = c = soma = cont = x1 = x2 = x3 = x4 = 0
while c >= 0:
    c = int(input('Insira um número inteiro. (Negativo para parar): '))
    cont += 1
    # Maior e menor números inseridos
    if cont == 1:
        maior = menor = c
    elif c > maior:
        maior = c
    elif menor > c >= 0:
        menor = c
    # Abaixo: quadrantes entre 0 e 100 pedidos pela questão
    if c in range(0, 26):
        x1 += 1
    elif c in range(26, 51):
        x2 += 1
    elif c in range(51, 76):
        x3 += 1
    elif c in range(76, 101):
        x4 += 1

print(f'O maior dentre os números foi {maior} e o menor foi {menor}')
print(f'A quatidade de números entre 0-25 foi: {x1}, entre 26-50 foi: {x2}, entre 51-75: {x3} e entre 76-100: {x4}')
print('Programa encerrado')
