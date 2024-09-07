from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
   return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        precio = request.form['precio']
        inventario = request.form['inventario']
        descuento = request.form['descuento']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO productos VALUES(%s,%s,%s,%s,%s)''',(id, nombre, precio, inventario, descuento))
        mysql.connection.commit()
        cursor.close()
        return f"Datos guardados con exito!!"
    
@app.route('/productos', methods = ['POST','GET'])
def productos():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM productos''')
        myresult = cursor.fetchall()
        for x in myresult:
         print(x)
        cursor.close()
        return "Hola mundo"

    if request.method == 'POST':
        return f"Datos recolectados"


app.run(debug=True, port=5000)
