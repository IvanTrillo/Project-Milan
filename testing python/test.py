import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="test"
)

mycursor = mydb.cursor() #Es como una variable que apunta

# Esto crea una base de datos de nombre 'test1'    mycursor.execute("CREATE DATABASE test1")

#Esto crea una tabla *Minimo 2  
mycursor.execute("CREATE TABLE empleados (nombre VARCHAR(255), direccion VARCHAR(255))")

'''
#Esto inserta en la tabla customers

nombre = input("Ingrese el nombre > ")
addrs = input("Ingrese la direccion > ")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (nombre, addrs)
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

#Esto altera la tabla customers
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
'''

'''
#Esto muestra todo lo que hay en una tabla
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

'''

'''
#Esto muestra todo lo que hay en ciertas columnas, notese que no utilice el id

mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''

'''
#Esto muestra todo lo que hay en la tabla que address sea 'Calle23'
sql = "SELECT * FROM customers WHERE address='Calle23'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''

'''
#Esto borra de la tabla todo lo que tenga address = 'Calle23'
Recordatorio que se debe utilizar mybd.commit para hacer cambios a la bd

sql = "DELETE FROM customers WHERE id='2'"
mycursor.execute(sql)
mydb.commit()
'''

'''
#Esto elimina la tabla
sql = "DROP TABLE customers"

mycursor.execute(sql)
'''



'''
#Esto sobreescribe la tabla customers
sql = "UPDATE customers SET address ='Canyon 123' WHERE address = 'Highway 21' "
mycursor.execute(sql)
mydb.commit()
'''

