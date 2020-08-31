'''Imprima um programa que lê um valor n inteiro e positivo
e que calcula a seguinte soma:  S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.
O programa deve escrever cada termo gerado e o valor final de S'''
soma=0
n=int(input('Digite um número natural '))
for c in range(1,n+1):
    x=1/c
    soma+=x
    #print('Termo gerado(',c,'):',x,'.',end=' ')
    print('Termo gerado({}):{:.4f}.'.format(c,x),end=' ')
print('O total é{:.5f}'.format(soma))
