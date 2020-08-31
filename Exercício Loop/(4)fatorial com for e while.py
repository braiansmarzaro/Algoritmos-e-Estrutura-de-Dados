#import factorial from math
num=int(input('Insira um número natural '))
result=1
n=1
'''for n in range(1,num+1):
    result*=n
    print(result,'(*',n,')')'''
    
while n<=num:
    result*=n
    n+=1
    print(result,end=' ')
    print('(*',n-1,')')