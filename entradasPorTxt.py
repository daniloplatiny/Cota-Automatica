#######################################################
### COTA AUTOMATICA COM BASE NO API DO GOOGLE       ###
### Arquivo - Input                                 ###
#######################################################

entrada = open('Entradas.txt')
linhas = entrada.readlines()
i = 0
while  i != len(linhas):
    if 'endereco =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        endereco = base[1]
        endereco = endereco[0:len(endereco)-1]
        endereco = endereco.replace(" ", "")
    if 'enderecoFinal =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        enderecoFinal = base[1]
        enderecoFinal = enderecoFinal[0:len(enderecoFinal)-1]
        enderecoFinal = enderecoFinal.replace(" ", "")
    if 'KEY =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        KEY = base[1]
        KEY = KEY[0:len(KEY)-1]
        KEY = KEY.replace(" ", "")
    if 'inicio =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        inicio = base[1]
        inicio = inicio[0:len(inicio)-1]
        inicio = int(inicio.replace(" ", ""))
    if 'limite =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        limite = base[1]
        limite = limite[0:len(limite)-1]
        limite = int(limite.replace(" ", ""))
    if 'numZona =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        numZona = base[1]
        numZona = numZona[0:len(numZona)-1]
        numZona = int(numZona.replace(" ", ""))
    if 'letraZona =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        letraZona = base[1]
        letraZona = letraZona[0:len(letraZona)-1]
        letraZona = letraZona.replace(" ", "")
    if 'correcaoDatum =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        correcaoDatum  = base[1]
        correcaoDatum  = correcaoDatum[0:len(correcaoDatum )-1]
        correcaoDatum  = int(correcaoDatum.replace(" ", ""))
    if 'altitudeH =' in linhas[i]:
        base = linhas[i].split("=",1 ) #Endereco do arquivo a ser lido
        altitudeH = base[1]
        altitudeH = altitudeH[0:len(altitudeH)-1]
        altitudeH = int(altitudeH.replace(" ", ""))
    i += 1

##################CORRECAO POR REGIAO##########################################
##Para correcao por regiao informe os pontos pedidos.
## COORDENADAS DO EPANET
#XY ponto a106
x = 611907.00
y = 8393590.00
#XY ponto a335
x1 = 611240.00
y1 = 8392580.00
#XY ponto BFF271
x2 = 609817.00
y2 = 8391570.00
#XY ponto BFF1216
x3 =610822.00
y3 =8391300.00
#XY ponto BFF1073
x4 =680328.00
y4 =8152760.00
#XY ponto BFF1253
x5=681160.00
y5=8152650.00

#COORDENADAS DO GOOGLE EARTH
#XY ponto a106
referenciaX = 611870.0
referenciaY = 8393562.27

#XY ponto a335
referenciaX1 =611202.09
referenciaY1 =8392538.76
#XY ponto XGG2243
referenciaX2 = 609770.33
referenciaY2 = 8391525.11
#XY ponto XGG1892
referenciaX3 = 610772.88
referenciaY3 = 8391256.72

referenciaX4 = 681115.60
referenciaY4 = 8152594.74

referenciaX5 = 681115.60
referenciaY5 = 8152594.74

teste = 0

def imprimiTeste():
    print(teste)