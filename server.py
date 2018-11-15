import datetime
import json

from flask import jsonify
from flask import Flask
from flask import request

from flaskext.mysql import MySQL
from flask_cors import CORS

from register import registerSomeone
from login import checkLogin
from utility import jsonifyViajes

app = Flask(__name__)
mysql = MySQL(app)
CORS(app)

# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
app.config['MYSQL_DATABASE_DB'] = 'TaxiUnico'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

#Scan a single device, receive ip address
@app.route("/")
def hello():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Cliente WHERE username = \"AaronUser\";")
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return str(data[1]+'\n')


# Validates user exists so it can login
# If credentials are valid, send home page.
@app.route("/login", methods = ['POST'])
def login():
    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get Json from request
    req = request.json
    print("User Request: ")
    print(req)

    # Get parameters from post request
    username = str(req['username'])
    password = str(req['password'])
    registrationType = str(req['registrationType'])

    # Receive Json with user data or False if user incorrect
    jsonSession = checkLogin(username, password, registrationType, cursor)

    # Returning session print
    print("Session: \n" + jsonSession)

    # Close db connection and cursor
    cursor.close()
    conn.close()

    if( jsonSession is None ) :
        return "Handle error here pl0x"

    return jsonSession


# Validates user doesn't exists so it can create it
# If user doesn't exist, create new entry in db with credentials
@app.route("/register", methods = ['POST'])
def register():
    id_admin = None

    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get Json from request
    req = request.json
    print("User Request: ")
    print(req)

    # Get parameters from post request
    username = str(req['username'])
    password = str(req['password'])
    firstName = str(req['firstName'])
    lastName = str(req['lastName'])
    sex = str(req['cellphone'])
    registrationType = str(req['registrationType'])

    # Convert date to database format
    dateArgument = str(req['date'])
    date = str(datetime.datetime.strptime(dateArgument , '%Y-%m-%d').date())

    if ( registrationType == 'T' ) :
        id_admin = str(req['id_admin'])

    isCorrect = registerSomeone(username, password, firstName, lastName, sex, date, registrationType, id_admin, cursor)

    if ( isCorrect is not False ) :
        conn.commit()

    return isCorrect


# Endpoint which returns every Trip, it assumes db never empty
# Ordered in descending order (Newest first)
@app.route("/getAllViajes", methods = ['GET'])
def viajes():

    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Create query
    query = "SELECT * FROM Viaje ORDER BY fechaYhora DESC;"
    cursor.execute(query)
    queryData = cursor.fetchall()

    print(queryData)

    return jsonifyViajes(queryData)

# Get every trip a user has made, key = username
# Ordered in descending order (Newest first)
@app.route("/getViajesFromCliente", methods = ['GET'])
def viajesCliente():

    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get username entered by user, assume username aways exists
    username = request.args.get('username')

    # Create query which returns viajes from client username
    query = "SELECT * FROM Viaje WHERE id_cliente = (SELECT id_cliente FROM Cliente WHERE username = " + username + ") ORDER BY fechaYhora DESC;"
    cursor.execute(query)
    queryData = cursor.fetchall()

    print(queryData)

    return jsonifyViajes(queryData)

# Get every trip a taxi driver has made, key = username
# Ordered in descending order (Newest first)
@app.route("/getViajesFromTaxista", methods = ['GET'])
def viajesTaxista():

    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get username entered by user, assume username aways exists
    username = request.args.get('username')

    # Create query which returns viajes from client username
    query = "SELECT * FROM Viaje WHERE id_taxista = (SELECT id_taxista FROM Taxista WHERE username = " + username + ") ORDER BY fechaYhora DESC;"
    cursor.execute(query)
    queryData = cursor.fetchall()

    print(queryData)

    return jsonifyViajes(queryData)
