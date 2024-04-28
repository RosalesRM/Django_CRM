# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 
import mysql.connector

# Establecer la conexión con el servidor MySQL
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""  # Contraseña de tu servidor MySQL
)

# Preparar un objeto cursor
cursorObject = dataBase.cursor()

# Crear una base de datos
cursorObject.execute("CREATE DATABASE IF NOT EXISTS oblivion")

# Cerrar el cursor y la conexión
cursorObject.close()
dataBase.close()

print("Base de datos creada correctamente")
