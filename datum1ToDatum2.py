import utm
import math
import entradas

latitude = []
longitude = []

#Dados WGS84
semi_eixo2 = 6.3781370e+06
achat2 = 3.35281066e-03

# Dados SAD69
semi_eixoSad =6.3781600e+06
achatSad = 3.35289187e-03
deltaxSad = 6.735000e+01
deltaySad = -3.880000e+00
deltazSad = 3.822000e+01

#Altura media da regiao
h1 = entradas.altitudeH

# Dados SIRGAS2000
semi_eixoSirgas =6.3781370e+06
achatSirgas = 3.35281068e-03
deltaxSirgas = 0.478
deltaySirgas = 0.491
deltazSirgas = -0.297


#SIRGAS2000	6.3781370e+06	3.35281068e-03	0.000000e+00	0.000000e+00	0.000000e+00"
#SAD69	6.3781600e+06	3.35289187e-03	-6.735000e+01	3.880000e+00	-3.822000e+01",



# Epanet 340066.24 8458078.89  , 340421.82 8458360.59
# Earth 340030.66 8458010.94  , 340368.02 8458330.28


def sad2wgs84(coordenadaX,coordenadaY):
    i = 0
    while i < len(coordenadaX):
        lat, lon = utm.to_latlon(coordenadaX[i],coordenadaY[i],entradas.numZona,entradas.letraZona)
        lat = math.radians(lat)
        lon = math.radians(lon)
        #calcula coordenadas geocentricas cartesianas no datum 1
        equad1 = 2 * achatSad - math.pow(achatSad,2)
        n1 = semi_eixoSad/math.sqrt(1-equad1*math.pow(math.sin(lat),2))
        x1 = (n1+h1)*math.cos(lat)*math.cos(lon)
        y1 = (n1+h1)*math.cos(lat)*math.sin(lon)
        z1 = (n1*(1-equad1)+h1)*math.sin(lat)

        #calcula coordenadas geocentricas cartesianas no datum 2
        x2 = x1 - deltaxSad
        y2 = y1 - deltaySad
        z2 = z1 - deltazSad

        #calcula coordenadas geodesicas no datum 2
        equad2  = 2 * achat2 - math.pow(achat2,2)
        lat2 = lat

        n2 = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))
        lat2 = math.atan((z2 + n2*equad2*math.sin(lat2))/math.sqrt(x2*x2 + y2*y2))
        d = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))- n2

        while abs(d)> 0.000000000001:
            n2 = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))
            lat2 = math.atan((z2 + n2*equad2*math.sin(lat2))/math.sqrt(x2*x2 + y2*y2))
            d = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))- n2

        lon2 = math.atan(y2/x2)
        h2 = h1

        latitude.append(math.degrees(lat2))
        longitude.append(math.degrees(lon2))
        i += 1

    return latitude, longitude



def sirgas2wgs84(coordenadaX,coordenadaY):
     i = 0
     while i > len(coordenadaX):
        lat, lon = utm.from_latlon(coordenadaX[i],coordenadaY[i])

        #calcula coordenadas geocentricas cartesianas no datum 1
        equad1 = 2 * achat1 - math.pow(achat,2)
        n1 = semi_eixo/math.sqrt(1-equad1*math.pow(math.sin(lat),2))
        x1 = (n1+h1)*math.cos(lat)*math.cos(lon)
        y1 = (n1+h1)*math.cos(lat)*math.sin(lon)
        z1 = (n1*(1-equad1)+h1)*math.sin(lat)

        #calcula coordenadas geocentricas cartesianas no datum 2
        x2 = x1 - deltax1
        y2 = y1 - deltay1
        z2 = z1 - deltaz1

        #calcula coordenadas geodesicas no datum 2
        equad2  = 2 * achat2 - math.pow(achat2,2)
        lat2 = lat

        n2 = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))
        lat2 = math.atan((z2 + n2*equad2*math.sin(lat2))/math.sqrt(x2*x2 + y2*y2))
        d = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))- n2

        while abs(d)> 0.000000000001:
            n2 = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))
            lat2 = math.atan((z2 + n2*equad2*math.sin(lat2))/math.sqrt(x2*x2 + y2*y2))
            d = semi_eixo2/math.sqrt(1-equad2*math.pow(math.sin(lat2),2))- n2

        lon2 = math.atan(y2/x2)
        h2 = h1

        latitude.append(lat2)
        longitude.append(lon2)

        return latitude,longitude



