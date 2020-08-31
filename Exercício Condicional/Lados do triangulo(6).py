print('Insira o valor dos 3 lados do triangulo')
a=float(input('primeiro lado '))
b=float(input('segundo lado '))
c=float(input('terceiro lado '))
cond=(a>(b+c) or b>(a+c) or c>(a+b))
if a==b==c:
    print( 'Triangulo Equilátero')
if a>(b+c) or b>(a+c) or c>(a+b):
    print('Lados não formam triângulo')
if a!=b and b!=c and not(cond ):
    print('Triângulo Escaleno')
if a==b!=c or a==c!=b or b==c!=a and not cond:
    print('triangulo Isósceles')