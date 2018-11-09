import datetime

from flask import jsonify
from flask import Flask
from flask import request

from flaskext.mysql import MySQL
from flask_cors import CORS

from register import registerSomeone
from login import checkLogin

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
    return str(data[1])


# Validates user exists so it can login
# If credentials are valid, send home page.
@app.route("/login", methods = ['POST'])
def login():
    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get parameters from post request
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    registrationType = str(request.args.get('registrationType'))

    # Receive Json with user data or False if user incorrect
    isCorrect = checkLogin(username, password, registrationType, cursor)

    # Close db connection and cursor
    cursor.close()
    conn.close()

    return isCorrect


# Validates user doesn't exists so it can create it
# If user doesn't exist, create new entry in db with credentials
@app.route("/register", methods = ['POST'])
def register():
    id_admin = None

    # Connect to db and get cursor
    conn = mysql.connect()
    cursor = conn.cursor()

    # Get parameters from post request
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    firstName = str(request.args.get('firstName'))
    lastName = str(request.args.get('lastName'))
    sex = str(request.args.get('sex'))
    dateArgument = str(request.args.get('date'))
    registrationType = str(request.args.get('registrationType'))
    date = str(datetime.datetime.strptime(dateArgument , '%Y%m%d').date())

    if ( registrationType == 'T' ) :
        id_admin = str(request.args.get('id_admin'))

    isCorrect = registerSomeone(username, password, firstName, lastName, sex, date, registrationType, id_admin, cursor)

    if ( isCorrect is not False ) :
        conn.commit()

    return isCorrect
