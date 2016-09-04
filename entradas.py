#######################################################
### COTA AUTOMATICA COM BASE NO API DO GOOGLE       ###
### Arquivo - Input                                 ###
#######################################################


#Endereco do arquivo a ser lido
endereco = 'Atual.inp'
#endereco = 'C:\\Users\\Danilo\\Desktop\\Estagio\\Ipora.inp'
#Endereco do arquivo de saida
enderecoFinal = 'Novo.inp'
#enderecoFinal = 'C:\\Users\\Danilo\\Desktop\\Estagio\\IporaCotado.inp'

#Chave do Google
#key = 'AIzaSyAr9B4WvxBlC5wi4gy__vRJAvrbe6kBQW8'
key = 'AIzaSyD-z50JAHdKGCbRTwDL91N9qkZNjM4dGNA' #Chave 2
#key = 'AIzaSyCAM_CQeD4oVE_9L3VsLKGeQP0wZ00irHc'


# Matricula e Senha
matricula = 'm807141'
senha = 'danilo142536'
autenticaoProxy = False

#Nó inicial e nó final a ser cotado.
limite  = 494
inicio = 0 # Primeiro nó é o o 0

#Informacoes para conversao para UTM
numZona = 22
letraZona ='K'

#Metodo Utilizado. Escolha o metodo para corrigir as coordenadas do cadastro
correcaoDatum = 0 # 0 para nao realizar conversao , 1 para converter SAD para sirgas
manual = 0 # 1 para manual , zero para utilizar DATUM

#########CONVERSAO DE DATUM#####################################################
#Se o metodo escolhido for  conversao de DATUM, descomente o DATUM de entrada
# datumEntrada = 'Sirgas2000'
# datumEntrada = 'SAD69'
altitudeH = 400  # Altitude media da regiao
#################################################################################

##################CORRECAO POR REGIAO##########################################
##Para correcao por regiao informe os pontos pedidos.
## COORDENADAS DO EPANET
#Ponto 1
epanetX1 = 492637.00
epanetY1 = 8185840.00

#Ponto 2
epanetX2 = 492643.00
epanetY2 = 8185480.00


#COORDENADAS DO GOOGLE EARTH
#Ponto 1 XY
referenciaX1 = 488414.09
referenciaY1 = 8186066.28
#Ponto 2 XY
referenciaX2 = 488388.40
referenciaY2 = 8185707.63
