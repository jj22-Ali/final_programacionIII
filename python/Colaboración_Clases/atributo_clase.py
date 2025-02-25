
class Cliente:

    cuentasSupendidas = []

    def __init__(self, cod_Cliente, nombre_cliente):
        self.cod_cliente = cod_Cliente
        self.nombre_cliente = nombre_cliente

    def imprimir(self):
        print(f'Codigo de cuenta {self.cod_cliente}')
        print(f'Nombre del titular: {self.nombre_cliente}')
        self.esta_suspendido()
    
    def suspender(self):
        Cliente.cuentasSupendidas.append(self.cod_cliente)

    def esta_suspendido(self):
        if self.cod_cliente in Cliente.cuentasSupendidas:
            print('Esta suspendido')
        else:
            print('No esta suspendido')
            print('-'*20)


cliente1 = Cliente(1, 'Mario')
cliente2 = Cliente(2, 'Juan')
cliente3 = Cliente(3, 'Romina')
cliente4 = Cliente(4, 'Susana')

cliente2.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()