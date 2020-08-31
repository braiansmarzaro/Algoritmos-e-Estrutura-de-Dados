"""Leia um número inteiro positivo e responda se o mesmo é primo ou não.
Parar quando for digitado um número negativo
(um número é primo se ele é divisível somente por ele mesmo e por 1"""
c=1
num=int(input('Número: '))
cont = 0
while c < ((num + 1)//2):

    if num % c == 0:
        cont += 1
        if c == num or c == 1:
            continue
    c+=1
    print(num, 'é divisível por', c)
    print('O número', num, 'foi divisível por', cont-2, 'número(s), além de 1 e o próprio',num)
    if cont == 2:
        print('O número digitado é primo\n')
    else:
        print('O número digitado não é primo\n')
    num = int(input('Número: '))