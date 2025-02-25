

"""
class Vehiculo:
    def __init__(self, marca, color, placa):
        self._marca = marca
        self.color = color
        self.placa = placa


coche = Vehiculo('ford', 'rojo', '1av232c')
print(coche.marca)
"""

"""
# Para ocultar métodos y atributos de elxterioe se usa doble guión bajo __ en el comienzo de su nombre. ESto hará que Python los interprete como "privados"

class Clase:
    __atributo_clase = 'Hola'
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

mi_clase = Clase('que tal')


print(mi_clase.atributo_clase)
print(mi_clase.atributo_instancia)

"""

# Deocradores - Setter

class Bebidas: 
    def __init__(self):
        self.__bebida = 'naranja'

    @property
    def favorita(self):
        return f'La bebida favorita es {self.__bebida}'
    
    @favorita.setter
    def favorita(self, bebida):
        self.__bebida = bebida


obj1 = Bebidas()
print(obj1.favorita)