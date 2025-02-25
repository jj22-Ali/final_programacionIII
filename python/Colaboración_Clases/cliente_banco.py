class Cliente:
    def __init__(self, titular):
        self.titular = titular
        self.monto = 0

    def ingresar(self, monto):
        self.monto = self.monto + monto

    def sacar(self, monto):
        self.monto = self.monto - monto

    def mostrar(self):
        return self.monto
    
    def imprimir(self):
        print(f'El usuario {self.titular}, tiene en el banco: ${self.monto}')


class Banco:
    def __init__(self):
        self.cliente1 = Cliente('Mario')
        self.cliente2 = Cliente('Luis')
        self.cliente3 = Cliente('Alberto')

    def operar(self):
        self.cliente1.ingresar(100)
        self.cliente2.ingresar(100)
        self.cliente3.ingresar(100)
        self.cliente3.sacar(3)
    
    def depositos_totales(self):
        total = self.cliente1.mostrar() + self.cliente2.mostrar() + self.cliente3.mostrar()
        print(f'El total despositado en el banco es: {total}')
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

#programa
banco1 = Banco()
banco1.operar()
banco1.depositos_totales()