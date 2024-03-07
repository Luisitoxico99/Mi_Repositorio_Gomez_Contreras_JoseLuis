
def alumnos_profesores(profesor, sustituto, *args):
    print("Profesor: " + profesor)
    print("sustituto: " + sustituto)
    for x in args:
        print("Alumno: " + x)
        
lista_alumnos=["Andy","Luis","Maria","Yera"]

alumnos_profesores("Juan Jose", "Armando", *lista_alumnos)