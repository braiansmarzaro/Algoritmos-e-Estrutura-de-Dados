code=int(input('Insira o código de cargo: '))
salario=float(input('Insira o salário inicial: '))
#code101='Gerente'
#code102='Engenheiro'
#code103='Técnico'
if code==101:
    salario2=1.1*salario
if code==102:
    salario2=1.2*salario
if code==103:
    salario2=1.3*salario
elif(code):
    salario2=1.4*salario
print('O antigo salário era de',salario,'reais')
print('O novo salário é de', salario2,'reais', end="")
print('. A diferença foi de', salario2-salario,'reais')