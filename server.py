from flask import jsonify
from flask import Flask
from flask import request

from flaskext.mysql import MySQL
from flask_cors import CORS

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

    # Make query and fetch result
    cursor.execute("SELECT * FROM Cliente WHERE username = \"" + username + "\";")
    dataUser = cursor.fetchone()

    # Assign db data variables
    dbUser = str(dataUser[1])
    dbPassword = str(dataUser[2])

    # Log data
    print ("User input\n username: " + username + " \n password: " + password)
    print ("Db data\n username: " + dbUser + " \n password: " + dbPassword)

    # Close db connection and cursor
    cursor.close()
    conn.close()

    # Quick validation of correct credentials
    if (username == dbUser and password == dbPassword) :
        return "Yes"

    return "No"
