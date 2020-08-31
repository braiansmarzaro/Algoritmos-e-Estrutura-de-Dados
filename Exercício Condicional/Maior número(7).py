print('digite 3 números inteiros')
a=int(input('primeiro número '))
b=int(input('segundo número '))
c=int(input('terceiro número '))
if a>b and a>c:
    print(a)
if b>a:
    if b>c:
        print(b)
if c>a and c>b:
    print(c)