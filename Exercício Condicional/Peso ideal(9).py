sexo=(input('Insira o genero(m ou f)'))
h=float(input('insira a altura: '))
homem=(72.7 * h) - 58
mulher=(62.1 * h) - 44.7
if sexo==str('m'):
    print('O peso ideal seria de ',homem,'kg')
if sexo==str('f'):
    print('O peso ideal seria de ',mulher, 'kg')   
