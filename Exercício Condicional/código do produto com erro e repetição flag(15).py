'''Lê o código de diversos produtos e apresenta a soma dos valores'''
from time import sleep

# code=(input(' digite o código do produto: ').strip().upper()) #Lê o código inserido
qnt = total = 0

while True:
    code = (input(' digite o código do produto[0 para PARAR]: ').strip().upper())
    if code == '0':
        break
    while code in ('ABCD', 'KLMP', 'QRST', 'XYPK'):  # condição para somar os valores

        qnt = int(input('insira a quantidade: '))
        if qnt <= 0:
            print('Error 404, quantity not found')

        elif qnt > 0:
            if code == 'ABCD':
                total += 5.3 * qnt
                print(f'O preço parcial é {total:.2f} reais')
            if code == 'XYPK':
                total += 6.0 * qnt
                print(f'O preço parcial é {total:.2f} reais')
            if code == 'KLMP':
                total += 3.2 * qnt
                print(f'O preço parcial é {total:.2f} reais')
            if code == 'QRST':
                total += 2.5 * qnt
                print(f'O preço parcial é {total:.2f} reais')
        break
        # code=(input('Digite um código ')).strip().upper()

        # print('O preço total é',total,'reais')
        # code=(input('Digite um código: ')).strip().upper()

    if code not in ('ABCD', 'KLMP', 'QRST', 'XYPK', '0'):  # and code!=0:

        print('Error 404, code not found\n')
        # code=(input('Digite um código ')).strip().upper()
        sleep(.5)
print(f'O preço total é R${total:.2f}'.replace('.',','))
