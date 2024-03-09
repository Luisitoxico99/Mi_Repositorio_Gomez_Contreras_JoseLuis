
class Usuarios:
    
    def  _init_(self,nombre,edad):
       self.nombre = nombre
       self.edad = edad
    
    def muestra_datos(self):
        print("El nombre de usuario es: " + self.nombre , self.edad)

usuario1= Usuarios("Ramon",21)
   
print(usuario1.nombre, usuario1.edad)
    
del usuario1.edad
    