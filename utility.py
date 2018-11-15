import json

def getTable(registrationType) :
    if ( registrationType == 'U' ) :
        return "Cliente"
    elif ( registrationType == 'T' ) :
        return "Taxista"
    elif ( registrationType == 'A' ) :
        return "Admin"
    else :
        return "None"

def jsonifyUserSession(data):
    info={}
    info['id']=data[0]
    info['username']=data[1]
    info['password']=data[2]
    info['name']=data[3]
    info['lastName']=data[4]
    info['sex']=data[5]
    return json.dumps(info)

def jsonifyTaxiSession(data):
    info={}
    info['id']=data[0]
    info['username']=data[1]
    info['password']=data[2]
    info['name']=data[3]
    info['lastName']=data[4]
    info['sex']=data[5]
    info['id_admin']=data[6]
    return json.dumps(info)

def jsonifyViajes(data):
    info=[]
    for d in data :
        viaje={}
        viaje['id']=d[0]
        viaje['fechaYhora']=str(d[1])
        viaje['destino']=d[2]
        viaje['origen']=d[3]
        viaje['costoPorKilometro']=d[4]
        viaje['id_cliente']=d[5]
        viaje['id_taxista']=d[6]
        viaje['id_carro']=d[7]
        info.append(viaje)

    return json.dumps(info)

def jsonifySingleID(data):
    info={}
    info['id']=data
    return json.dumps(info)
