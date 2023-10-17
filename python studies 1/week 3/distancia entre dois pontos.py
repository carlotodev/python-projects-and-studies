# calcula a distância entre 2 pontos de um ponto cartesiano e diz se a distância entre eles é longa ou curta, baseado em uma distância de 10 pontos
import math

x1 = int(input("insira aqui o primeiro eixo x: "))
y1 = int(input("insira aqui o primeiro eixo y: "))
x2 = int(input("insira aqui o segundo eixo x: "))
y2 = int(input("insira aqui o segundo eixo y: "))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d >= 10:
    print("longe")
else:
    print("perto")