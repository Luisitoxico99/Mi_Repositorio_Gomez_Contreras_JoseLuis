import sqlite3

# Conectarse a la base de datos
conexion = sqlite3.connect('ejemplo.db')

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar una consulta para recuperar todos los registros de una tabla
cursor.execute('SELECT * FROM empleados')

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
