'''Jogar JO KEN PÔ com o computador'''
import random
from time import sleep

tupla = ('pedra', 'papel', 'tesoura')
maq = random.choice(tupla)

c = True
while c is True:
    print('Jo')
    sleep(.5)
    print('Ken')
    sleep(.5)
    print('PÔ')
    sleep(.5)
    user = str(input('ESCOLHA SUA ARMA: ')).strip().lower()
    maq = str(random.choice(tupla))
    print(user)
    print('*=' * 15)
    print('Escolhi...', end=' ')
    sleep(0.5)
    print(f'{maq.upper()}!')

    if user == 'pedra':  # pedra
        print('Você escolheu PEDRA!')
        print('*=' * 15)
        if maq == 'pedra':
            print('EMPATE!\n')
        if maq == 'tesoura':
            print('Parabéns, você me venceu!')
        if maq == 'papel':
            print('HAHAHA, YOU LOSE')
    if 'pa' in user:  # papel
        print('Você escolheu PAPEL!')
        print('*=' * 15)
        if maq == 'pedra':
            print('Parabéns, você me venceu!')
        if maq == 'tesoura':
            print('HAHAHA, YOU LOSE')
        if maq == 'papel':
            print('EMPATE!\n')

    if user == 'te':  # tesoura
        print('Você escolheu TESOURA!')
        print('*=' * 15)
        if maq == 'pedra':
            print('HAHAHA, YOU LOSE')
        if maq == 'tesoura':
            print('EMPATE!\n')
        if maq == 'papel':
            print('Parabéns, você me venceu!')
    print('Jogar novamente?')
    play = str(input('\n'))
    if play.lower() in 'naono':
        c = False
    elif play in 'simyes':
        c = True
    print('PROCESSANDO...')
    sleep(.8)
print('Foi divertido jogar com você!')
print('FIM DE JOGO')
