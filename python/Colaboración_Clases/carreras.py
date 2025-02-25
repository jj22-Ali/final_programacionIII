class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        self.__fecha_inicio = fecha

    @property
    def fechaInicio(self):
        return self.__fecha_inicio

    @fechaInicio.setter
    def fechaInicio(self, fecha):
        if fecha < 2006:
            self.__fecha_inicio = 2006
        else:
            self.__fecha_inicio = fecha


class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = {}  # Contendrá tuplas {codigo, materia}

    def agregar_materias(self, codigo, materia):  # Cambiar el orden de los parámetros
        self.materias[codigo] = materia

    def mostrar_materias(self):
        print(f'Materias de la carrera {self.nombre}:')
        for codigo, materia in self.materias.items():
            print(f'Código: {codigo}, Materia: {materia.nombre}, Profesor: {materia.profesor}, Fecha de inicio: {materia.fechaInicio}')


# Crear una carrera
carrera1 = Carrera('Ingeniería en Sistemas')

# Crear materias
algebra = Materia('Algebra', 'Juan Quinteros', 2002)
fisica = Materia('Fisica', 'Rogelio Juan', 2023)
programacion = Materia('Programación', 'Oscar Maleandrok', 2025)

# Agregar materias a la carrera (código primero, luego la materia)
carrera1.agregar_materias(201, algebra)
carrera1.agregar_materias(321, fisica)
carrera1.agregar_materias(131, programacion)

# Mostrar las materias de la carrera
carrera1.mostrar_materias()

# Acceder a la fecha de inicio de una materia
print(f'La fecha de inicio de {algebra.nombre} es {algebra.fechaInicio}')