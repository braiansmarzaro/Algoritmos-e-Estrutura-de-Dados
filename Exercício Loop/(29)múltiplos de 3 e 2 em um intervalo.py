'''solicite dois números entre 1 e 100 ao usuário e
imprima a quantidade de múltiplos de 2 ou 3 entre eles,
desconsiderando os números que sejam dos dois ao mesmo tempo.
#Não# Assuma que o usuário vá digitar os dois números em ordem crescente.'''
# 25 linhas para ler os números independente da ordem e dentro da margem
while True:
    n1 = int(input('Digite o primeiro número[999 para parar]: '))
    men = mai = n1
    if n1 == 999:
        break
    while men < 1 or mai > 100:  # Detecta se o número é válido
        print('Entrada inválida.', end=' ')
        if n1 > 100:
            print('O número deve ser menor que 101')
        if n1 < 1:
            print('O número deve ser maior que 0')
        n1 = int(input('Digite o primeiro número: '))
        men = mai = n1
    n2 = int(input('Digite o segundo número: '))
    while n2 > 100 or n2 <= 0:
        print('Entrada inválida.', end=' ')
        if n2 > 100:
            print('O número deve ser menor que 101')
        if n2 <= 0:
            print('O número deve ser maior que 0')
        n2 = int(input('Digite o segundo número: '))
    if n1 > n2:
        men = n2
    elif n1 < n2:
        mai = n2

    for c in range(men, mai + 1):
        if c % 2 == 0 and not c % 3 == 0:
            print(c, end=', ')
        elif c % 3 == 0 and not c % 2 == 0:
            print(c, end=', ')
    print()
print('Programa encerrado')