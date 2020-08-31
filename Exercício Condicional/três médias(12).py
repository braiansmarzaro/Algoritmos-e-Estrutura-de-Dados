print('escolha a operação que deseja realizar\n','1 para média aritmética, 2 para média ponderada, 3 para média harmônica')
func=int(input())

n1=float(input('insira a primeira nota '))
n2=float(input('insira a segunda nota '))
n3=float(input('insira a terceira nota '))

ma=(n1+n2+n3)/3
mp=(n1*3+n2*3+n3*4)/10
mh=3/(1/(n1+n2+n3))

if func==1:
    print('a média aritmética de',n1,n2,'e',n3,' é',ma)
if func==2:
    print('a média ponderada de',n1,n2,'e',n3,' é',mp)
if func==3:
    print('a média harmônica de',n1,n2,'e',n3,' é',mh)
