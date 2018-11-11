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

def jsonifySession(data):
        info={}
        info['id']=data[0]
        info['username']=data[1]
        info['password']=data[2]
        info['name']=data[3]
        info['lastName']=data[4]
        info['sex']=data[5]
        return json.dumps(info)    
