
class MiPerro:
    def hablar(self):
        print('Guau' * 3)

class MiPato:
    def hablar(self):
        print('Cuack' * 3)

class MiVaca:
    def hablar(self):
        print('Muu' * 3)

def hacer_hablar(x):
    x.hablar()

mi_perro = MiPerro()
hacer_hablar(mi_perro)  # Salida: GuauGuauGuau

mi_pato = MiPato()
hacer_hablar(mi_pato)  # Salida: CuackCuackCuack

mi_vaca = MiVaca()
hacer_hablar(mi_vaca)  # Salida: MuuMuuMuu