print('Insira o valor dos 3 lados do triangulo')
a=float(input('primeiro lado '))
b=float(input('segundo lado '))
c=float(input('terceiro lado '))
import math

cond=a>(b+c) or b>(a+c) or c>(a+b) #condição de não existencia

if a==b==c:
    print( 'Triangulo Equilátero')
    print('área=',math.sqrt(3)*(a**2)/4)

if cond:
    print('Lados não formam triângulo')
    print('area indeterminada')    
if a!=b and b!=c and not(cond ) and not (a==b or b==c or c==a):
    print('Triângulo Escaleno')
    print('area=')
if a==b!=c or a==c!=b or b==c!=a and not cond:
    print('triangulo Isósceles')
    if a==b:
       altura=math.sqrt(a**2-(c/2)**2)
       print('área=',c*altura/2)
    if b==c:
        altura=math.sqrt(b**2-(a/2)**2)
        print('área=',a*altura/2)
    if a==c:
        altura=math.sqrt(a**2-(b/2)**2)
        print('área=',b*altura/2)

