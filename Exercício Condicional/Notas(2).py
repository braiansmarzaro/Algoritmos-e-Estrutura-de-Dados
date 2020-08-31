print('insira a primeira nota')
n1=float(input())
print('insira a segunda nota')
n2=float(input())
print('insira a terceira nota')
n3=float(input())
soma = n1 + n2 + n3
media = soma / 3
print('a média é ', (n1+n2+n3)/3)
if media>=7:
    print('Parabéns, você foi aprovado')
if media<7 and media>=5:
    print('Você está de recuperação')
if media < 5:
    print('Reprovado')