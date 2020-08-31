"""Escrever um programa que leia um valor N inteiro e positivo e
 que calcule e imprima o valor de E = 1 + 1 / 1! + 1 / 2! + 1 / 3! +...+ 1 / N! """
from math import factorial

while True:
    cont = 0
    soma = 1
    n = int(input('Insira um número natural: '))
    if n < 0:
        break
    print('1+')
    for c in range(1, n + 1):
        soma += 1 / factorial(c)
        print(f'({c}) +1/{c}! =', soma,)
    print('\n')
