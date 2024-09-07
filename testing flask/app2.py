from flask import Flask, render_template

app = Flask(__name__)


#Forma estandar de mostrar un texto plano
@app.route('/')
def hola_mundo():
   return "<h1>Hola mundo!</h1>"

#Se pueden hacer 'ruteos' para mostrar cierta informacion
@app.route('/pagina2')
def pagina2():
    return " Pagina dos!"

#Con <> se declara una variable que podemos usar despues
@app.route('/usuario/<nombre_usuario>')
def mostrar_nombre_usuario(nombre_usuario):
    return f'Usuario {nombre_usuario}'

#se pueden convertir a int, float, path y strings (este es el default)
@app.route('/id/<int:id>')
def mostrar_id(id):
    return f"La id es {id}"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
