'''Escrever um programa que leia 10 valores, um de cada vez,
e conte quantos deles estão no intervalo [10,20]
e quantos deles estão fora do intervalo,
escrevendo estas informações ao final. '''

cont=0
for c in range(1,11):
    n=int(input('Insira um número inteiro '))
    if c<10:
        print('Faltam',10-c,'números')
    if n>=10 and n<=20:
        cont+=1
print('A quantidade de números dentro do intervalo foi de',cont)
print('A quantidade de números fora do intervalo foi de',10-cont)
