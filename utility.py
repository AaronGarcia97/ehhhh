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
    info['email']=data[6]
    info['cellphone']=data[7]
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
    info['email']=data[7]
    info['cellphone']=data[8]
    return json.dumps(info)

def jsonifyViajes(data):
    info = []
    for d in data :
        viaje={}
        viaje['id']=d[0]
        viaje['fechaYhora']=str(d[1])
        viaje['destino']=d[2]
        viaje['origen']=d[3]
        viaje['costoPorKilometro']=d[4]
        viaje['id_cliente']=d[5]
        viaje['id_taxista']=d[6]
        info.append(viaje)

    return json.dumps(info)

# Function returns json of Users
def jsonifyUsers(data):
    info = []
    print("Data retrived from db(users): " + str(data))
    for u in data :
        user={}
        user['id']=u[0]
        user['username']=u[1]
        user['password']=u[2]
        user['name']=u[3]
        user['lastName']=u[4]
        user['sex']=u[5]
        user['date']=str(u[6])
        user['email']=u[7]
        user['cellphone']=u[8]
        info.append(user)

    return json.dumps(info)

# Function that returns json of Taxistas
def jsonifyTaxistas(data):
    info = []
    for t in data :
        taxista = {}
        taxista['id']=t[0]
        taxista['username']=t[1]
        taxista['password']=t[2]
        taxista['name']=t[3]
        taxista['lastName']=t[4]
        taxista['sex']=t[5]
        taxista['id_admin']=t[7]
        taxista['email']=t[8]
        taxista['cellphone']=t[9]
        info.append(taxista)

    return json.dumps(info)

# Function returns single object json, with object's name
def jsonifySingleObject(data, object):
    info={}
    print("Data retrived from db (" + str(object) + "): " + str(data))
    info[object]=data
    return json.dumps(info)
