
class usuarios: #Se crea la clase
    def __init__(usuario, nombre, edad):
        usuario.nombre = nombre      #Las variables son:
        usuario.edad = edad                        
        
    def muestra_datos(datos):
        print("El nombre del usuario es: " + datos.nombre, datos.edad) #Se hace print del texto y las variables 
        
usuario1 = usuarios("Juancho", 76)    #Datos de usuario
usuario1.muestra_datos()                

usuario1.edad = 65                    #Declaramos variable
usuario1.muestra_datos()              #Se muestran los valores
