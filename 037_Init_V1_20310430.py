
class usuarios():    #Creacion de clase
    
    def __init__(self,nombre,pin):
        self.nombre=nombre  #Variaboles de la clase
        self.pin=pin
        
    def saludo(self):
        print("Saludos" + self.nombre + "Sesion iniciada correctamente")  #Se imprimen los textos junto con el nombre
    
    def despedida(self):
        print(self.nombre + "Se ha cerrado sesion") #Se imprime el nombre y los textos del estado de la sesion
        
usuario1 = usuarios ("Luis","1234")  #Datos de variables

usuario2 = usuarios ("Julieta","3546") #Datos de usuario2

usuario1.saludo()  #Usuarios y acciones
usuario2.saludo()
usuario1.despedida()  
