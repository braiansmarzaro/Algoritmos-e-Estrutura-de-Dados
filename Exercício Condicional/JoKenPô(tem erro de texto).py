'''Jogar JO KEN PÔ com o computador'''
import random
from time import sleep

lista=('pedra','papel','tesoura')
maq=random.choice(lista)

c=True
while c == True:
    print('Jo'); sleep(.5)
    print('Ken');sleep(.5)
    print('PÔ');sleep(.5)
    user=str(input(' ')).strip().lower()[1]
    maq=random.choice(lista)
    print('*='*15)
    print('Escolhi...',end=' ')
    
    print('{}!'.format(maq).upper())
    
    if user in'pe': #pedra
        print('Você escolheu PEDRA!')
        print('*='*15)
        if maq == 'pedra':
            print('EMPATE!\n' )
        if maq == 'tesoura':
            print('Parabéns, você me venceu!')
        if maq in 'papel':
            print( 'HAHAHA, YOU LOSE')
    if user in 'pa': #papel
            print('Você escolheu PAPEL!')
            print('*='*15)
            if maq is 'pedra': print('Parabéns, você me venceu!')
            if maq is 'tesoura': print( 'HAHAHA, YOU LOSE')
            if maq is 'papel':print('EMPATE!\n' )

    if user in'te':#tesoura
        print('Você escolheu TESOURA!')
        print('*='*15)
        if maq is 'pedra': print( 'HAHAHA, YOU LOSE')
        if maq is 'tesoura':print('EMPATE!\n' )
        if maq is 'papel': print('Parabéns, você me venceu!')
    
    print('Jogar novamente?')
    
    play=input('\n')
    if play in 'Naonaono':
        c = False
    elif play in 'simyes':
        c = True
    print('PROCESSANDO...');sleep(.8)
print('Foi divertido jogar com você!')
print('FIM DE JOGO')
    