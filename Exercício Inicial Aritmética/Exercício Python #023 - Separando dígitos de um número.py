'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.'''

num=int(input('Insira um número: '))
u=num%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Total de:')
print(f'{u} unidades')
print(f'{d} dezenas')
print(f'{c} centenas')
print(f'{m} milhares')