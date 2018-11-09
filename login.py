from flaskext.mysql import MySQL
from utility import getTable

def checkLogin(username, password, registrationType, cursor) :
    table = getTable(registrationType)

    # Nunca debería entrar aquí
    if( table == "None" ) :
        return False

    # Create query
    query = "SELECT * FROM " + table + " WHERE username = \"" + username + "\";"
    cursor.execute(query)
    dataUser = cursor.fetchone()

    if( dataUser is None ) :
        return False

    # Assign db data variables
    dbUser = str(dataUser[1])
    dbPassword = str(dataUser[2])

    # Log data
    print ("User input\n username: " + username + " \n password: " + password)
    print ("Db data\n username: " + dbUser + " \n password: " + dbPassword)

    # Quick validation of correct credentials
    if (username == dbUser and password == dbPassword) :
        # Create JSON with user info for sessions and return it
        return "Yes"


    return "No"
