class Alumno: 
    nro_alumnos = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        Alumno.nro_alumnos += 1  # agregamos un alumno

    def __str__(self):
        return f'Nombre:{self.nombre} (nota: {self.nota})'
    
    # dar de baja el alumno
    def __del__(self):
        Alumno.nro_alumnos -= 1;
        print('Alumno dado de baja')
        print('{Almuno.nro_alumnos} legajos restantes')

    #estado del alumno

    def mostrar_estado(self):
        if self.nota <= 4:
            print(f'El estado de {self.nombre} es regular')
        elif self.nota < 9:
            print(f'El estado de {self.nombre} es bueno')
        else:
            print(f'El estado de {self.nombre} es excelente')


# Programa principal

alumno1 = Alumno('German Bin Gonzales', 8)
alumno2 = Alumno('Franco Bobadilal', 2)
print(alumno1)
print(alumno2)
alumno1.mostrar_estado()
alumno2.mostrar_estado()
input('Pulse enter para salir')
