# Deivid Braian Smarzaro; Eng. Metal. 2020.1
# Referências: https://brasilescola.uol.com.br/matematica/medidas-dispersao-variancia-desvio-padrao.htm
"""1. Ler dois valores inteiros m e n, entre 1 e 20. Criar um vetor de nome Vet1 de
tamanho m e um vetor de nome Vet2 de tamanho n. Os dois vetores deverão
conter valores inteiros. """
from random import randint

m = int(input("Digite um número inteiro entre 1 e 20: "))
while m not in range(1, 21):  # Valida a entrada entre 1 e 20
    print(f'Número inválido, tente novamente.')
    m = int(input("Digite um número inteiro entre 1 e 20: "))
n = int(input("Digite um segundo número inteiro entre 1 e 20: "))
while n not in range(1, 21):  # Valida a entrada entre 1 e 20
    print(f'Número inválido, tente novamente.')
    n = int(input("Digite um segundo número inteiro entre 1 e 20: "))

vet1 = [0] * m
vet2 = [0] * n
'''2. Preencher o vetor Vet1 com valores inteiros aleatórios entre 100 e 120 e o vetor
Vet2 com valores inteiros aleatórios entre 150 e 170.'''
for c in range(len(vet1)):
    vet1[c] = randint(0, 20) + 100
for c in range(len(vet2)):
    vet2[c] = randint(0, 20) + 150
'''3. Imprimir os vetores Vet1 e Vet2. Para tanto,
crie uma função (def), de nome ImprimeVetor, que receba dois parâmetros: um
vetor a ser impresso e um texto a ser impresso antes do conteúdo do vetor. Os
valores dos elementos do vetor a serem impressos deverão estar separados por
virgulas. Faça uma chamada à função para imprimir Vet1 e outra chamada para
imprimir Vet2.'''


def imprimevetor(vet, txt):  # Cria a função imprimevetor
    return f'{txt}:{vet}'.replace('[', '').replace(']', '')


print(f'{imprimevetor(vet1, "vet1")}\n'
      f'{imprimevetor(vet2, "vet2")}')  # Chama a função duas vezes
'''4. Criar um vetor de nome Soma, de tamanho m, se m ≥ n, ou n, se n > m.'''
if n > m:
    soma = [0] * n
else:
    soma = [0] * m
'''5. Preencher o vetor Soma de tal forma que cada elemento i do mesmo contenha a
soma dos elementos das i-ésimas posições de Vet1 e Vet2, se existirem, ou seja, Soma[i] = Vet1[i] + Vet2[i].'''
for c in range(len(soma)):
    if len(vet1) >= len(vet2):  # Confere qual vetor é maior
        if c <= len(vet2) - 1:  # Confere quando acaba o menor vetor
            soma[c] = vet1[c] + vet2[c]
        else:
            soma[c] = vet1[c]  # Quando acabar o menor, soma[i] recebe o valor do maior vetor
    elif len(vet2) > len(vet1):  # Confere qual vetor é maior
        if c <= len(vet1) - 1:  # Confere quando acaba o menor vetor
            soma[c] = vet1[c] + vet2[c]
        else:
            soma[c] = vet2[c]  # Quando acabar o menor, soma[i] recebe o valor do maior vetor
'''6. Imprimir o vetor Soma, conforme layout do exemplo abaixo, utilizando a função
ImprimeVetor, criada no item 3.'''
print(imprimevetor(soma, 'Soma'))
'''7. Calcular e imprimir a soma e a média aritmética simples dos valores armazenados
no vetor Soma'''
tot = 0
for c in soma:
    tot += c  # soma os termos dentro do vetor Soma
media = tot / len(soma)
print(f'Soma dos valores: {tot}\nMédia aritmética simples: {media:.2f}')
'''8. Calcular e imprimir a variância populacional 
e o desvio padrão populacional dos valores armazenados no vetor Soma.'''
varpop = desvio = cmenosmedia = 0
for c in soma:
    cmenosmedia += (c - media) ** 2  # Realiza a somatoria de (Xn-media)²
varpop = cmenosmedia / len(soma)
desvio = varpop ** .5  # Desvio é a raiz quadrada da variação
print(f'Variância populacional: {varpop:.2f}\nDesvio padrão populacional: {desvio:.2f}')
'''9. Calcular e imprimir a média harmônica dos valores armazenados no vetor Soma'''
somaharmonica = mediaharm = 0
for c in soma:
    somaharmonica += 1 / c  # Soma os termos de Soma elevados a -1
mediaharm = (somaharmonica / len(soma)) ** -1
print(f'Média harmonica: {mediaharm:.2f}')
'''10. Calcular e imprimir a média ponderada dos valores armazenados em Soma,
de acordo com o seguinte critério, para cada i-ésimo valor armazenado no vetor:
a. Se Soma[i] contiver a soma de Vet1[i] + Vet2[i], o peso da posição será 3.
b. Se Soma[i] contiver somente um valor oriundo de Vet1[i], o peso da
posição será 2.
c. Se Soma[i] contiver somente um valor oriundo de Vet2[i], o peso da
posição será 1.'''
mediapond = somapond = peso = 0
for c in range(len(soma)):  # Soma somapond e peso de acordo com as especificações
    if len(vet1) - 1 >= c and c <= len(vet2) - 1:  # Len=ultima casa do vetor+1, ex len=2, ultima casa=1
        somapond += soma[c] * 3
        peso += 3
    elif len(vet1) - 1 >= c:  # Caso o vetor 1 seja o maior
        somapond += soma[c] * 2
        peso += 2
    elif len(vet2) - 1 >= c:  # Caso o vetor 2 seja o maior
        somapond += soma[c]
        peso += 1
mediapond = somapond / peso
print(f'Média Ponderada: {mediapond:.2f}')
'''11. Imprimir o conteúdo do vetor Soma em ordem crescente, conforme layout do
exemplo abaixo, utilizando a função ImprimeVetor, criada no item 3.'''
# Criando um bubble sort
for j in range(0, len(soma) - 1):
    for c in range(0, len(soma) - 1):
        if soma[c] >= soma[c + 1]:
            aux = soma[c]
            soma[c] = soma[c + 1]
            soma[c + 1] = aux
print(imprimevetor(soma, "Soma ordenada"))
'''12. Calcular e imprimir a frequência absoluta e relativa dos valores armazenados no vetor Soma. '''
absolut = 0  # Frequência absoluta
for c in range(len(soma)):  # Lê os numeros do vetor soma
    for j in range(len(soma)):  # Lê uma segunda vez para comparação com a primeira
        if soma[j] == soma[c]:  # Caso o número seja encontrado, conta-se(número sera encontrado pelo menos 1 vez)
            absolut += 1
    if soma[c] != soma[c - 1]:  # Se o número atual for diferente do anterior, imprime, caso contrário, passa adiante
        # Imprime os resultados solicitados
        print(f'Valor = {soma[c]}. Freq. Abs. = {absolut}. Freq. relat. = {absolut / len(soma):.4f}')
    absolut = 0  # Reinicia o contador
if len(soma) == 1:
    print(f'Valor = {soma[0]}. Freq. Abs. = {1}. Freq. relat. = {1:.4f}')
