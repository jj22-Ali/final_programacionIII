
"""
1.Encapsulamiento y metodo Privados(python)

crea una llamada CuentaBancaria con los siguiente atributos y métodos:

* AtributosPrivados:
__saldo: Rrepresenta al saldo actual de la cuenta
__titular: Nombre del Titular de la Cuenta

* Metodos publicos:

consultar_saldo(): Retornar el saldo acutal
depositar(moonto): Incrementa el saldo en la cantidad especificada.
retirar(monto): Decrementa el saldo asegurandse de que no sea negativo. Si el monto a retir es mayor qeu el saldo, muestre un mensaje de error
"""


class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo       # Atributo privado

    @property
    def titular(self):
        return self.__titular  # Acceder al atributo privado

    @titular.setter
    def titular(self, titular):
        self.__titular = titular  # Modificar el atributo privado

    @property
    def saldo(self):
        return self.__saldo  # Acceder al atributo privado

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo  # Modificar el atributo privado

    def consultarSaldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f'Depositar de exitoso, saldo actual: ${self.__saldo}')
        else:
            print('Debe ingresar un monto mayor que cero')

    def retirar(self, sacar):
        if sacar > 0:
            if self.__saldo > sacar:
                self.__saldo -= sacar
                print(f'Retiro de exitoso, saldo actual: ${self.__saldo}')
            else:
                print('No puede sacar mas de lo que tiene')
        else:
            print('El monto debe ser mayor a 0')
# Crear una instancia de CuentaBancaria
cliente = CuentaBancaria('Juan', 10000)


print(cliente.consultarSaldo())

cliente.depositar(4000)
cliente.retirar(2000)
