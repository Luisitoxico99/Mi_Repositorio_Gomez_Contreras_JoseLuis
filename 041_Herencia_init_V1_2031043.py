
# Esta es la superclase
class Usuarios:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
	self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios):
	def __init__(self, nombre, apellidos, instagram):
		self.nombre = nombre
	self.apellidos = apellidos
	self.instagram = instagram
	

	