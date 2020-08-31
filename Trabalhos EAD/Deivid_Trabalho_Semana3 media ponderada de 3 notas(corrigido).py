# Deivid Braian Smarzaro. Eng. Metal 2020.1

# 1.Ler o nome e 3 notas de avaliação de um aluno. A nota é um valor inteiro entre 0 e 100.
nome = str(input('Digite seu nome: ').capitalize())
print('Insira notas entre 0 e 100, por favor')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

# 2.Calcular e escrever o nome do aluno, suas notas e a média aritmética simples das notas lidas
media = (nota1 + nota2 + nota3) / 3
print(f'{nome}, suas notas foram {nota1}, {nota2}, e {nota3}. Sua média foi de {media}')

# 3. Calcular e escrever a média ponderada das 3 notas lidas.
# A maior nota terá peso 40, a segunda maior nota terá peso 35 e a menor nota terá peso 25.
# Caso existam notas iguais, pesos diferentes deverão ser atribuídos as mesmas.
maior = nota1
meio = nota2
menor = nota3
if nota1 > nota3 > nota2:
    meio = nota3
    menor = nota2
elif nota2 > nota1 >= nota3:
    maior = nota2
    meio = nota1
elif nota2 > nota3 > nota1:
    maior = nota2
    meio = nota3
    menor = nota1
elif nota3 > nota1 >= nota2:
    maior = nota3
    meio = nota1
    menor = nota2
elif nota3 > nota2 > nota1:
    maior = nota3
    meio = nota2
    menor = nota1
print(f'Maior={maior},meio={meio},menor={menor}')
mediapond = (maior * 40 + meio * 35 + menor * 25) / 100
print(f'A média ponderada das notas de {nome} é {mediapond}')
# 4. Escrever quais valores lidos estão acima da média aritmética calculada no item 2
cont = 0  # Conta quantas notas estão acima da média de notas do aluno
if nota1 > media:
    print('Nota 1 está acima da média!')
    cont += 1
if nota2 > media:
    print('Nota 2 está acima da média!')
    cont += 1
if nota3 > media:
    print('Nota 3 está acima da média!')
    cont += 1

# 5.Escrever quantos valores lidos estão acima da média aritmética calculada no item 2
print(f'{nome} tem {cont} nota(s) acima de sua média aritmética')
