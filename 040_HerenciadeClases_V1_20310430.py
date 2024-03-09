
class Usuarios:
    def _nit_ (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def muestra_datos(self):
       print("El nombre de usuario es: " + self.nombre, "y tiene", self.edad)
       
       usuario1=Usuarios("Luis", 24)
       
       usuario1.muestra_datos()
       
       class Usuarios_premium(Usuarios):
           pass
       usuario2 = Usuarios_premium("Maria", 21)
       
       usuario2.muestra_datos()
           