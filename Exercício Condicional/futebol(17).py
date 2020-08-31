print('Insira o nome do time')
time1=input()
gp=int(input('Número de gols feitos: ') ) 
gn=int(input('Número de gols sofridos: '))   
vf=int(input('Número de vitórias fora de casa: '))  
vc=int(input('Número de vitórias em casa: '))
e=int(input('Número de empates: '))

ponto1 = 5*gp - gn + 3*vf + 2*vc + e


