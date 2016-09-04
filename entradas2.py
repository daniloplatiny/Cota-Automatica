
#######################################################
### COTA AUTOMATICA COM BASE NO API DO GOOGLE       ###
#######################################################
import xyToUTM
import entradas
import datum1ToDatum2
import googleElevation2


#Variaveis auxiliares
i = 0
ativado = False
layout = False # Se ja passou pelo epanet , 0 nao 1 sim

#Listas
nomeNo = [] # Lista com os nos
coordenadaX = [] # Lista das coordenadas X
coordenadaY = [] # Lista com as coordenadas Y
nos=[] # Lista de strings com o trecho contendo as informcacoes (nos, coordendas)
arquivoNovo = []
limite  = entradas.limite
inicio = entradas.inicio

#Endereco do arquivo a ser lido
endereco =entradas.endereco

# Abre o arquivo
arquivo = open(endereco)

#Le o arquivo e salva em uma lista
linhas = arquivo.readlines()

#Separa as informacoes que necessitamos do arquivo INP
while  i != len(linhas):
    if '[COORDINATES]' in linhas[i]:
        ativado = True
        if 'Node' in linhas[i+1]:
            i +=2
            layout = True
        else:
            i += 1
    if ativado == 1:
        nos.append(linhas[i])
        if '\n' == linhas[i+1]:
           break
    i += 1

contador = 0
for linha in nos:
   if  contador > limite:
       break
   if contador >= inicio and layout == True:
       if len(linha.split('\t')) == 3 :
           a,b,c = linha.split('\t')
           nomeNo.append(a)
           coordenadaX.append(float(b))
           coordenadaY.append(float(c))
   else:
       if contador >= inicio and len(linha.split()) == 3 :
         a,b,c = linha.split()
         nomeNo.append(a)
         coordenadaX.append(float(b))
         coordenadaY.append(float(c))

   contador += 1

#Converte coordenada original para UTM
if(entradas.correcaoDatum == 1):
    latitude , longitude = xyToUTM.xy2UTM(coordenadaX,coordenadaY)
else:
    latitude , longitude = datum1ToDatum2.sad2wgs84(coordenadaX,coordenadaY)

#Obtem a cota utilizando o api do google
cotas = googleElevation2.cota(latitude,longitude)

#Variaveis auxiliares
roda = 0
quantidadeNo = 1
contador = 0
#Monta o novo arquivo inp para ser gravado
for pontos in linhas:
    if roda > inicio + 4  and contador < len(cotas):
        aux = pontos.split(' ')
        roda = 1 + roda
        arquivoNovo.append(aux[1] +' \t \t'+ str (round(cotas[contador],2))+'\n')
        contador += 1
    else:
        arquivoNovo.append(pontos)
        roda = 1 + roda


arquivo.close()


#Endereco do arquivo a ser lido
endereco = entradas.enderecoFinal
#Salva o novo arquivo
arquivo = open(endereco,'w')
arquivo.writelines(arquivoNovo)


arquivo.close()

print('FIM')

