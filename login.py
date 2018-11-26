import json

from flaskext.mysql import MySQL
from utility import getTable
from utility import jsonifyTaxiSession, jsonifyUserSession

def checkLogin(username, password, registrationType, cursor) :
    table = getTable(registrationType)

    # Nunca deberia entrar aqui
    if( table == "None" ) :
        print("here1")
        return json.dumps({}), status.HTTP_500_INTERNAL_SERVER_ERROR

    # Create query
    query = "SELECT * FROM " + table + " WHERE username = \"" + username + "\";"
    cursor.execute(query)
    dataUser = cursor.fetchone()

    if( dataUser is None ) :
        print("here2")
        return json.dumps({}), status.HTTP_500_INTERNAL_SERVER_ERROR

    # Assign db data variables
    dbUser = str(dataUser[1])
    dbPassword = str(dataUser[2])

    # Log data
    print ("User input\n username: " + username + " \n password: " + password)
    print ("Db data\n username: " + dbUser + " \n password: " + dbPassword)

    # Quick validation of correct credentials
    if (username == dbUser and password == dbPassword) :
        # Create JSON with user info for sessions and return it
        if (registrationType == 'T') :
            return jsonifyTaxiSession(dataUser)

        return jsonifyUserSession(dataUser)


    return {}
