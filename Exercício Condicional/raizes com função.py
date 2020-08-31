import math
def p(txt):
    print(txt)
def raizes():    
    p('insira a equação de segundo grau ax²+bx+c')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    raiz1=int(-b + math.sqrt(b**2 -4*a*c))/(2*a)
    raiz2=int(-b - math.sqrt(b**2 -4*a*c))/(2*a)
    print('as raízes são',raiz1,' e',raiz2)

raizes()

