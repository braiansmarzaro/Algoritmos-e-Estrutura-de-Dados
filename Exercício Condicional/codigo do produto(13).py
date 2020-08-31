print(' digite o código do produto')
code=(input())
qnt=int(input('insira a quantidade '))  
total=float()
def conditional():
    if code=='1001':
        total=5.32*qnt
        print('O preço total é',total,'reais')
    elif code=='1324':
        total=6.45*qnt
        print('O preço total é',total,'reais')
    elif code=='6548':
        total=2.37*qnt
        print('O preço total é',total,'reais')
    elif code=='0987':
        total=5.32*qnt
        print('O preço total é',total,'reais')
    elif code=='7623':
        total=6.45*qnt
        print('O preço total é',total,'reais')
    else:
        print('Error 404, code not found')
      
conditional()

