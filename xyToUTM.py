import utm
import entradas

# ## Coordenadas do Epanet
# #XY ponto 1086
# x = entradas.x
# y = entradas.y
# #XY ponto BFF748
# x1 = entradas.x1
# y1 = entradas.y1
# #XY ponto BFF271
# x2 = entradas.x2
# y2 = entradas.y2
# #XY ponto BFF1216
# x3 =entradas.x3
# y3 =entradas.y3
# #XY ponto BFF1073
# x4 =entradas.x4
# y4 =entradas.y4
# #XY ponto BFF1253
# x5 =entradas.x5
# y5 =entradas.y5
#
#
# #Coordenadas Referencia do googgle earth
# #XY ponto 1
# referenciaX = entradas.referenciaX
# referenciaY = entradas.referenciaY
# #XY ponto 2
# referenciaX1 =entradas.referenciaX1
# referenciaY1 =entradas.referenciaY1
# #XY ponto 3
# referenciaX2 = entradas.referenciaX2
# referenciaY2 = entradas.referenciaY2
# #XY ponto 4
# referenciaX3 = entradas.referenciaX3
# referenciaY3 = entradas.referenciaY3
#
# referenciaX4 = entradas.referenciaX4
# referenciaY4 = entradas.referenciaY4
#
# referenciaX5 = entradas.referenciaX5
# referenciaY5 = entradas.referenciaY5
#
#
# #Entradas basicas
numZona = entradas.numZona
letraZona = entradas.letraZona
# altCoordenadasX = []
# altCoordenadasY = []
latitude = []
longitude = []
#
# #Calculo das diferencas entre epant e google
# deltay = y - referenciaY
# deltax = x - referenciaX
#
# deltay1 = y1 - referenciaY1
# deltax1 = x1 - referenciaX1
#
# deltay2 = y2 - referenciaY2
# deltax2 = x2 - referenciaX2
#
# deltay3 = y3 - referenciaY3
# deltax3 = x3 - referenciaX3
#
# deltay4 = y4 - referenciaY4
# deltax4 = x4 - referenciaX4
#
# deltaXLista = [deltax,deltax1,deltax2,deltax3,deltax4]
# deltaYLista = [deltay,deltay1,deltay2,deltay3,deltay4]


# Coordenada 1
#  Epanet  x 678714.00   y 8259840.00
# Google 679306.78  8259529.47

# Coordenada 2
#  Epanet 679351.00   8259580.00
# 678668.87   8259795.84


# Epanet 677574.00 8257460.00
# Google 677535.49 8257413.00

def xy2UTM(coordenadaX,coordenadaY):

    i = 0
    while i < len(coordenadaY):
     lat,long =  utm.to_latlon(coordenadaX[i],coordenadaY[i],entradas.numZona,entradas.letraZona)
     latitude.append(lat)
     longitude.append(long)
     i += 1

       # #Encontra qual delta usar para x
       #  varX =abs( coordenadaX[i] - referenciaX)
       #  varX1 = abs(coordenadaX[i] - referenciaX1)
       #  varX2 = abs(coordenadaX[i] - referenciaX2)
       #  varX3 = abs(coordenadaX[i] - referenciaX3)
       #  listaVarx = [ varX,varX1,varX2,varX3]
       #  menorX = listaVarx.index(min(listaVarx))
       # #Encontra qual delta usar para y
       #  vary = abs(coordenadaY[i] - referenciaY)
       #  vary1 = abs(coordenadaY[i] - referenciaY1)
       #  vary2 = abs(coordenadaY[i] - referenciaY2)
       #  vary3 = abs(coordenadaY[i] - referenciaY3)
       #  listaVary = [ vary,vary1,vary2,vary3]
       #  menorY = listaVary.index(min(listaVary))
       #  #Adiciona a coordenada corrigida a uma lista
       #  altCoordenadasY.append(coordenadaY[i] - deltaYLista[menorY])
       #  altCoordenadasX.append(coordenadaX[i] - deltaXLista[menorX])
       #  #Converte a coordenada UTM ara lat e lon
       #  lat,long =  utm.to_latlon(altCoordenadasX[i],altCoordenadasY[i],entradas.numZona,entradas.letraZona)



    return latitude , longitude