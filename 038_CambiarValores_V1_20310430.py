
class usuarios:
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre
        usuario.edad = edad
        
    def muestra_datos(datos):
        print("El nombre del usuario es: " + datos.nombre, datos.edad)
        
usuario1 = usuarios("Juancho", 76)
usuario1.muestra_datos()

usuario1.edad = 65
usuario1.muestra_datos()