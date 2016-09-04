import math
import entradas

def translacao(coordenadaX,coordenadaY):
    deltaX = entradas.referenciaX1 - entradas.epanetX1
    deltaY = entradas.referenciaY1 - entradas.epanetY1
    i = 0
    testeX = coordenadaX[0]
    novoX = []
    novoY = []
    print(deltaX , deltaY)
    while i < len(coordenadaX):
        novoX.append(deltaX + coordenadaX[i])
        novoY.append(deltaY + coordenadaY[i])
        i = i +1
    return novoX, novoY

def produtoVetorial(vetor1,vetor2):
    return vetor1[0]*vetor2[0] + vetor1[1]*vetor2[1]

def comprimento(vetor):
    return math.sqrt(pow(vetor[0],2) + pow(vetor[1],2))

def vector(x1,y1,x2,y2):
    vetorx = x1 - x2
    vetory = y1 - y2
    vetor = [vetorx, vetory]
    return vetor

def angulo(vetor1, vetor2):
    return math.acos(produtoVetorial(vetor1,vetor2) /(comprimento(vetor1)*comprimento(vetor2)))

def rotacao(pontoX,pontoY,centroX,centroY,angulo):
    novoX = centroX +(pontoX - centroX)*math.cos(angulo) - (pontoY - centroY)*math.sin(angulo)
    novoY = centroY +(pontoX - centroX)*math.sin(angulo) +(pontoY - centroY)*math.cos(angulo)
    return novoX,novoY

def trans_rot(coordenadasX, coordenadasY):

    vetor1 = vector(entradas.referenciaX1,entradas.referenciaY1, entradas.referenciaX2, entradas.referenciaY2)  # Obtem o vetor de referencia
    vetor2 = vector(entradas.epanetX1,entradas.epanetY1,entradas.epanetX2,entradas.epanetY2) # Ontem o vetor do epanet
    ang = angulo(vetor1,vetor2) # Angulo entre os vetores

    novoX , novoY = translacao(coordenadasX,coordenadasY) # Translada os pontos
    finalX = []
    finalY = []

    # i = 0
    #
    # while i < len(novoX):
    #     x,y = rotacao(novoX[i], novoY[i], entradas.referenciaX1, entradas.referenciaY1, ang)
    #     finalX.append(x)
    #     finalY.append(y)
    #     i = i + 1

    return novoX, novoY

