class Persona:
    def __init__(self, identificacion, nombre, apellido, dni):
        self.id = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'{self.id} - DNI: {self.dni}, {self.apellido} {self.nombre}'


class alumnoTaller(Persona):
    def __init__(self, identificacion, nombre, apellido, dni, curso):
        Persona.__init__(self, identificacion, nombre, apellido, dni)
        self.curso = curso

    def __str__(self):
        return f'{self.id} - DNI - {self.dni}; {self.apellido}, {self.nombre}. Carrera:{self.curso}'
    

p1 = Persona( 12 , 'Juan Jose', 'Figueroa', 41345809)
print(p1)

n1 = alumnoTaller(32, 'Maria', 'Rolheiser', 34893218, 'Abogacia')
print(n1)