"Deivid Braian Smarzaro; Eng. Metal. 2020.1"
# Pede-se:
# 1. A distância total percorrida no trajeto de Botucatu a Catanduva;
# 2. A média de velocidade desenvolvida pelo veículo em todo o trajeto;
# 3. Os três trechos em que Ariovaldo atingiu a maior velocidade média por trecho
# Fonte: https://www.sunearthtools.com/pt/tools/distance.php#txtDist_1 (Cálculo da distância geodésica)
# Importante: Entre os pontos 49 e 50, o python não é capaz de obter a diferença precisamente,
# resultando em distância nula (dist=0)
import math

# Le arquivo do trabalho da semana 6 e escreve o seu conteúdo;Define qual o arquivo a ser aberto.
agenda = open("C:\\Users\\smar_\\Google Drive\\Engenharia\\Algoritmo e Estrutura de Dados\\Trabalhos EAD\\Semana "
           "6\\LeiturasGPS.csv", "r")

top1 = top2 = top3 = cont = veltot = vel = dist = disttot = 0
# Lê a primeira linha do arquivo, armazenando o conteudo na variável string linha
linha = agenda.readline()  # Lê a primeira linha do arquivo
numLeitA = int(linha.split(",")[0])
latA = float(linha.split(",")[1])
longA = float(linha.split(",")[2])
# Raio da terra utilizado será de R = 6.372,795477598 km
# Para o cálculo, a terra é considerada como uma esfera e seu raio é aproximado,
# e por isso o cáculo apresenta uma margem de erro com a realidade
R = 6372.795477598
# Distância(A, B) = R * arccos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(LongA - longB)), visto fonte
# Os ângulos utilizados são expressos em radianos.
# Conversão de graus para radianos é obtida através da função math.radians(). A distância será então:
# dist = R * math.acos(math.sin(math.radians(latA)) * math.sin(math.radians(latB)) + math.cos(math.radians(latA))
#          * math.cos(math.radians(latB)) * math.cos(math.radians(longA - longB)))

pontoa = pontob = ponto2a = ponto2b = ponto3a = ponto3b = ''  # Declara as coordenadas dos pontos para impressão
while linha != 'FIM':  # Enquanto o terminador "FIM" não for encontrado
    cont += 1  # Conta quantos trechos foram percorridos
    # Pega as três informações contidas na linha e armazena em variáveis
    linha = agenda.readline()  # Lê a linha consecutiva do arquivo e a armazena
    if linha != 'FIM':  # Não lê a linha fim, caso ela seja chamada dentro da presente repetição
        numLeitB = str(linha.split(",")[0])
        latB = float(linha.split(",")[1])
        longB = float(linha.split(",")[2])
    dist = R * math.acos(math.sin(math.radians(latA)) * math.sin(math.radians(latB)) + math.cos(math.radians(latA))
                         * math.cos(math.radians(latB)) * math.cos(math.radians(longA - longB)))

    disttot += dist  # Acumula a distancia total percorrida
    # Km/5min convertido para Km/h; Sua localização geográfica foi salva, rigorosamente, a cada 5 minutos.
    vel = dist * 12  # substitui vel = dist / (5/60); Marca a velocidade no trecho em Km/h
    veltot += vel  # Acumula a velocidade de todos os trechos para calcular a média aritmética
    #print(dist, vel, numLeitA)
    if vel > top1 or top1 == 0:  # Caso a velocidade lida seja maior que a maior atual, realiza os ajustes e armazena
        top3 = top2
        top2 = top1
        top1 = vel
        ponto3a = ponto2a
        ponto3b = ponto2b
        ponto2a = pontoa
        ponto2b = pontob
        pontoa = numLeitA
        pontob = numLeitB

    # Caso a velocidade lida seja maior que a segunda maior atual, apenas, realiza os ajustes e armazena
    elif vel > top2:
        top3 = top2
        top2 = vel
        ponto3a = ponto2a
        ponto3b = ponto2b
        ponto2a = numLeitA
        ponto2b = numLeitB
    elif vel > top3:  # Caso a velocidade lida seja maior que a terceira maior atual, apenas, realiza os ajustes
        top3 = vel
        ponto3a = numLeitA
        ponto3b = numLeitB
    # Armazena os valores B em A para a próxima comparação
    numLeitA = numLeitB
    latA = latB
    longA = longB

agenda.close()
print(f'A distância total percorrida no trajeto de Botucatu a Catanduva foi de {disttot:.3f} Km')
print(f'A média de velocidade desenvolvida pelo veículo durante o trajeto total foi de {veltot / (cont-1):.2f} Km/h')
print(f'A maior velocidade foi desenvolvida entre os pontos {pontoa} e {pontob}, com {top1:.3f}Km/h')
print(f'A segunda maior velocidade foi desenvolvida entre os pontos {ponto2a} e {ponto2b}, com {top2:.3f}Km/h')
print(f'A terceira maior velocidade foi desenvolvida entre os pontos {ponto3a} e {ponto3b}, com {top3:.3f}Km/h')
