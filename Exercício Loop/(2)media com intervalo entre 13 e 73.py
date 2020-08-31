'insira numeros até que haja um <=0,'
'tire a média aritmética dos numeros entre 13 e 73'

n=int(input('Insira um número inteiro positivo '))
if n>12 and n<74:
    soma=n
    cont=1
else:
    soma=0
    cont=0

print('Total de números válidos: ',cont)

while n>0:
    n=int(input('Insira um número inteiro '))
    
    if n>=13 and n<=73:
        soma=soma+n
        print('a soma é',soma,',',end=' ')
        cont+=1
        print('Total de números válidos: ',cont)
        
    elif n>0: #and n<13 or n>73: #cancaleado por não necessitar
        print('Este número não será somado.',end=' ')
        print('Total de números válidos:',cont)
        
#if:
print('A média aritmética dos números válidos é',soma/cont)