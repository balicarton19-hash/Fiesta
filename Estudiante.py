#camelCase para clases
#snape_case para canales

class Estudiante:
    #constructor - crea un objeto
    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno

        #tostring - representacio de texto
    def __str__(self):
        return f"{self.apellido_paterno} {self.nombre}"
