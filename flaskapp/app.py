from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_db'

mysql = MySQL(app)


@app.route('/')
def hello():
    return '<h1>Hello, Welcome to homepage !</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/doLogin', methods=['POST'])
def doLogin():

    email = request.form.get("email")
    password = request.form.get("password")

    cur = mysql.connection.cursor()
    resp = cur.execute(
        '''SELECT * from users where email=%s and password=%s;''', (email, password))
    if resp == 1:
        return render_template("home.html")
    else:
        return render_template("login.html", message="Login Failed")


app.run(debug=True)
