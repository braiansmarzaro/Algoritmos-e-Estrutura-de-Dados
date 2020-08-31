a=float(input('insira o valor de a '))
b=float(input('insira o valor de b '))
if b>a:
    a=b
    b=a
if a%b==0:
    print('são múltiplos')
if a%b!=0:
    print('não são multiplos')
