print('insira o nome do Aluno')
nome=input()
print('insira a primeira nota')
n1=float(input())
print('insira a segunda nota')
n2=float(input())
print('insira a terceira nota')
n3=float(input())
falta=int(input('insira o numero de faltas'))
soma = n1 + n2 + n3
media = soma / 3
print('a média é ', (n1+n2+n3)/3)
if media>=7:
    if falta<32:
        print('Parabéns,',nome,'foi aprovado')
    if falta>=32:
        print(nome,' foi reprovado por falta')
if media < 7 :
    print(nome,' foi Reprovado por média',end="")
    if falta>=32:
        print(' e por falta')


    
