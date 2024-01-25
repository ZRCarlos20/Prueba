instructores = []
class Instructor:
    def __init__(self):
        self.id = 0  
        self.nombre = ""
        self.apellido = ""
        self.curso = ""
        self.correo = ""
        
        
    def ingresar_instructor():
        instructores.append( Instructor())
        return instructores