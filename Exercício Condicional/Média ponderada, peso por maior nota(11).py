print('insira o código do aluno')
codigo=input()
print('insira a primeira nota')
n1=float(input())
print('insira a segunda nota')
n2=float(input())
print('insira a terceira nota')
n3=float(input())
soma = n1*4 + n2*3 + n3*3
if n1<n2 and n2>=n3:
    soma=n1*3 + n2*4 + n3*3
if n3>n1 and n3>n2:
    soma=n1*3 + n2*3 + n3*4
media = soma / 10
if media>=5:
    print('Parabéns,',codigo,' foi aprovado')
if media < 5:
    print(codigo,' foi reprovado')
print('As notas foram ',n1 ,',',n2,' e ',n3,end="")
print(' e a média foi de ',media)