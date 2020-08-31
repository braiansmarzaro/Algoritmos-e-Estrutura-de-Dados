'20 primeiros termos da série de Fibonacci'
'0,1,1,2,3,5,8,13,21,34,55,89'
'''O proximo termo é igual a soma dos dois termos anteriores,
começando em 0,1'''

a=0
b=1
for c in range(0,20):
    soma=a+b
    a=b
    b=soma
    print(soma,end=' ')