"""Deivid Braian Smarzaro. Eng Metal 2020.1"""
'''Semana 2:    2)Crie uma nova versão do algoritmo anterior, 
informando se o valor fornecido é divisível por 02, por 03, por 02 E por 03 ou nenhum dos dois.'''

num = int(input('Digite um número natural: '))

while num<0:
    print(f'Erro, o número deve ser natural')
    num = int(input('Digite um número natural: '))
if num == 0:
    print(f'0 não é divísivel por outro número que não seja 0')
elif num % 2 == 0 and num % 3 == 0:
    print(f'O {num} é divisível por 2 e 3, simultâneamente.')
elif num % 2 == 0:
    print(f'O {num} é divisível por 2, apenas')
    print(f'{num}/2 é ={num / 2}')
elif num % 3 == 0:
    print(f'O {num} é divisível por 3, apenas')
else:
    print(f'O {num} não é divisível por 2 ou 3.')


