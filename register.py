from flaskext.mysql import MySQL

from utility import getTable, jsonifySingleID

id_num = 100000069

# Creates new Client or Admin
def createClientOrAdmin(table, id_someone, username, password, firstName, lastName, sex, date, cursor) :
    query = "INSERT INTO " + table + " VALUES (\'" + id_someone + "\',\'" + username + "\',\'" + password + "\',\'" + firstName + "\',\'" + lastName + "\',\'" + sex + "\',\'" + date + "\');"
    print (table + ":\n" + query)
    cursor.execute(query)
    print ("User(" + id_someone + "): " + username + " succesfully created.")
    return id_someone



# Creates new Taxista
def createTaxista(table, id_someone, username, password, firstName, lastName, sex, date, id_admin, cursor) :
    query = "INSERT INTO " + table + " VALUES (\'" + id_someone + "\',\'" + username + "\',\'" + password + "\',\'" + firstName + "\',\'" + lastName + "\',\'" + sex + "\',\'" + date + "\',\'" + id_admin + "\');"
    print (table + ":\n" + query)
    cursor.execute(query)
    print ("User(" + id_someone + "): " + username + " succesfully created.")
    return id_someone


# Handles which function to call in order to register new user of any type correctly
# (types: Client, Taxista, Admin)
def registerSomeone(username, password, firstName, lastName, sex, date, registrationType, id_admin, cursor):
    global id_num
    table = ""
    id_someone = registrationType + str(id_num)

    # Assign correct table
    table = getTable(registrationType)
    if ( table == "None") :
        return False

    # Check if user doesnt exist
    query = "SELECT * FROM " + table + " WHERE username = \"" + username + "\";"
    cursor.execute(query)
    queryData = cursor.fetchone()

    print ("Im here")
    if ( queryData is None ) : # Create stuff
        id_num = id_num + 1
        if ( registrationType == 'U' or registrationType == 'A' ) :
            return jsonifySingleID(createClientOrAdmin(table, id_someone, username, password, firstName, lastName, sex, date, cursor))
        else :
            return jsonifySingleID(createTaxista(table, id_someone, username, password, firstName, lastName, sex, date, id_admin, cursor))

    # Don't create anything since username already exists
    return False
