class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

    def __str__(self):
        return f'Titulo:{self.titulo}, duracion:{self.duracion} min, años:{self.lanzamiento}'
    

class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas

    def agregar(self, p):
        Catalogo.peliculas.append(p)

    def mostra(self):
        for p in Catalogo.peliculas:
            print(p)

pelicula1 = Pelicula('El padrino', 200, 1972)
c = Catalogo([pelicula1])
c.mostra()

pelicula2 = Pelicula('Iron Man', 120, 2007)
c = Catalogo([pelicula2])
c.mostra()

pelicula3 = Pelicula('El padrino II', 220, 1974)
c = Catalogo([pelicula3])
c.mostra()
