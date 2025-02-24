class Padre: #superclase1
    def llevar(self):
        print('Papa me lleva a la escuela')

class Madre: #superclase2
    def  programar(self):
        print('Mama programa en python')


class Hijo(Padre, Madre):
    def amar(self):
        print('Amo a mis padre')


hijo1 = Hijo() #intacias hijos

hijo1.llevar()
hijo1.programar()
hijo1.amar()