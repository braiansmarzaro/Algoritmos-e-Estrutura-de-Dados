print("Duração do evento em segundos")
tempo=int(input())
horas=tempo//3600
minutos=tempo//60-horas*60
segundos=tempo-horas*3600-minutos*60
print('o tempo total é ',horas,'horas',minutos,'minutos',' e',segundos,'segundos')
