'''Lê o código de diversos produtos e apresenta a soma dos valores(contém erros)'''   

code=(input(' digite o código do produto: ').strip().upper()) #Lê o código inserido
qnt=0
total=float()
while code not in ('ABCD','KLMP','QRST','XYPK'):
        print('Error 404, code not found')
        code=(input('Digite um código ')).strip().upper()

while code in ('ABCD','KLMP','QRST','XYPK'): #condição para somar os valores
    
    qnt=int(input('insira a quantidade: '))
    if qnt<=0:
        print('Error 404, quantity not found')

    while qnt>0:
        if code== 'ABCD':
            total+=5.3*qnt
            print('O preço total é',total,'reais')
        if code =='XYPK':
            total+=6.0*qnt
            print('O preço total é',total,'reais')
        if code == 'KLMP':
            total+=3.2*qnt
            print('O preço total é',total,'reais')
        if code == 'QRST':
            total+=2.5*qnt
        code=(input('Digite um código ')).strip().upper()

    #print('O preço total é',total,'reais')
    #code=(input('Digite um código: ')).strip().upper()
        
    while code not in ('ABCD','KLMP','QRST','XYPK'):
        print('Error 404, code not found')
        code=(input('Digite um código ')).strip().upper()
    
print('O preço total é R${:.2f}'.format(total))
   