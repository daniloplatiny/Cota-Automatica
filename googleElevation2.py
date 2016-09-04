import urllib
from googlemaps import Client,elevation
import entradas

KEY = entradas.KEY
#KEY = entradas.KEY #Chave 2


def cota(latitude,longitude):
    gmaps = Client(key=KEY)
    aux=1
    cotas = []
    entrada = []
    while aux < len(latitude):
        if  (aux % 6 == 0 and aux!= 0):
            entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]))
            url = entrada[0] + entrada[1] + entrada[2] + entrada[3] + entrada[4] + entrada[5]
            a = gmaps.elevation(url)
            print (round(100*aux/(entradas.limite - entradas.inicio),2),'% ')
            for i in range(0,6):
                cotas.append(float(a[i].get('elevation')))
            del(entrada[:])
            del(a)
        else:
            entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]) + '|')
        aux +=1

    if len(latitude)== 1:
        entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]))
        url = entrada
        a = gmaps.elevation(url)
        cotas.append(float(a[0].get('elevation')))
        del(entrada[:])
        del(a)

    if len(entrada):

        entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]) + '|')
        url =entrada[0]
        aux5 = 0
        while aux5+1 < len(entrada) :
            url = url + entrada[aux5+1]
            aux5 +=1
        url = url[0:len(url)-1]
        a = gmaps.elevation(url)
        print (round(100*aux/(entradas.limite - entradas.inicio),2),'% ')
        aux2 = 0
        while  len(a):
             cotas.append(float(a[aux2].get('elevation')))
             aux2+=1
             aux +=1
             if aux2 == len(a):
                break

    print (round(100*(entradas.limite - entradas.inicio)/(entradas.limite - entradas.inicio),2),'% ')

    return cotas
