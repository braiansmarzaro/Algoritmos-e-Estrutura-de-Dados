# Deivid Braian Smarzaro; Eng. Metal 2020.1
'''1) Ler 50 números reais entre 700.0 e 1000.0, correspondendo aos valores diários de
fechamento das ações da companhia ACME, armazenando-os em um vetor de
nome vetEnt. Alternativamente, pode-se preencher os elementos do vetor com
valores aleatórios, entre 700.0 e 1000.0, obtidos através da função random() ou
equivalente, do módulo random. Podem ainda ser atribuídos valores fixos aos
elementos do vetor, desde que estejam entre 700.0 e 1000.0.
2) Criar um segundo vetor, de nome vetMMS, com 31 elementos do tipo float.
Armazenar no segundo vetor a Média Móvel Simples (MMS) dos últimos 20 dias
(MMS20), dos valores de fechamentos armazenados em vetE, começando pelo
vigésimo valor armazenado em vetEnt.
No cálculo da MMS20 de um dado dia, deve-se incluir o valor de fechamento do próprio dia.
3) Imprimir os valores diários de fechamento para cada dia e, ao lado do valor de
cada dia, o valor da MMS20 daquele dia, se existir. '''
from random import uniform, randint

media20 = 0  # Calcula a media dos ultimos 20 dias
vetEnt = [0] * 50
# Criar um segundo vetor, de nome vetMMS, com 31 elementos do tipo float para salvar a media20
vetMMS = [0.0] * 31
for c in range(0, 50):
    vetEnt[c] = uniform(700, 1000)  # Preenche a lista com números reais entre 700 e 1000
    if c >= 19:  # c=19 é o vigésimo número da lista
        for j in range(c - 19, c + 1):
            media20 += vetEnt[j]
        vetMMS[c - 19] = media20 / 20
        media20 = 0
print(f'{"Dia":<4}{"Fech.":^10}{"MMS20":>10}')
for c in range(1, 51):  # Do dia 1 ao 50
    print(f'{c:<5}R${vetEnt[c - 1]:^10.4f}', end='')  # c-1 pois o dia 1 inicia em 0
    if c >= 20:
        print(f' R${vetMMS[c - 20]:>8.3f}')
    else:
        print(f'{"-":^9}')
