import googlemaps
import entradas

KEY = entradas.KEY
cotas = []
gmaps = googlemaps.Client(key=KEY)


def cota(latitude,longitude):
    aux=0
    while aux < len(latitude):
        entrada = str(latitude[aux]) + ',' + str(longitude[aux])
        a = gmaps.elevation(entrada)
        print(a,aux)
        cotas.append(float(a[0].get('elevation')))
        aux+=1
    return cotas