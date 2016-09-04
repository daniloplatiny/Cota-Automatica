import urllib.request as req
import pprint
import json
import urllib.request
import entradas

KEY = entradas.key

base_url = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
chave =  '&key=' + KEY
location = '39.7391536,-104.9847034|39.7491536,-104.9847034|39.7591536,-104.9847034'
url = base_url + location + chave


def cota(latitude,longitude):

    if entradas.autenticaoProxy:
        urlprox = r'https://' + entradas.matricula.strip() + entradas.senha.strip() + '@proxy.saneago.com.br:8080'
        proxy = req.ProxyHandler({'https': urlprox})
        auth = req.HTTPBasicAuthHandler()
        opener = req.build_opener(proxy, auth, req.HTTPHandler)
        req.install_opener(opener)

    aux=1
    cotas = []
    entrada = []
    while aux < len(latitude):
        if  (aux % 6 == 0 and aux!= 0):
            entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]))
            location = entrada[0] + entrada[1] + entrada[2] + entrada[3] + entrada[4] + entrada[5]
            print(location)
            url = base_url + location + chave
            conn = req.urlopen(url)
            obj= conn.read().decode('utf8')
            obj = urllib.request.urlopen(url).read().decode('utf8')
            obj1 = json.loads(obj)
            a = obj1.get('results')
            print (round(100*aux/(len(latitude)),2),'% ')
            for i in range(0,6):
                cotas.append(float(a[i].get('elevation')))
            del(entrada[:])
            del(location)
        else:

            entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]) + '|')
        aux +=1
    if len(entrada):
        entrada.append(str(latitude[aux-1]) + ',' + str(longitude[aux-1]) + '|')
        location =entrada[0]
        aux5 = 0
        while aux5+1 < len(entrada) :
            location = location + entrada[aux5+1]
            aux5 +=1
        location = location[0:len(location)-1]
        url = base_url + location + chave
        obj = urllib.request.urlopen(url).read().decode('utf8')
        obj1 = json.loads(obj)
        a = obj1.get('results')
        print (round(100*(aux-1)/(len(latitude)),2),'% ')
        aux2 = 0
        while  len(a):
             cotas.append(float(a[aux2].get('elevation')))
             aux2+=1
             aux +=1
             if aux2 == len(a):
                break

    print (round(100*(entradas.limite - entradas.inicio)/(entradas.limite - entradas.inicio),2),'% ')


    return cotas