
class usuarios():
    
    def __init__(self,nombre,pin):
        self.nombre=nombre
        self.pin=pin
        
    def saludo(self):
        print("Saludos" + self.nombre + "Sesion iniciada correctamente")
    
    def despedida(self):
        print(self.nombre + "Se ha cerrado sesion")
        
usuario1 = usuarios ("Luis","1234")

usuario2 = usuarios ("Julieta","3546")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()
