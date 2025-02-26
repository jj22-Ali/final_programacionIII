
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
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def consultarSaldo(self):
        return print(f'El saldo actual de tu cuenta es {self.__saldo}')

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f'Doposito Exitoso. Su saldo actual es {self.__saldo}')
        else:
            print('Debes ingresar un monto mayor a 0')

    def retirar(self, monto):
        if monto > 0:
            if self.__saldo > monto:
                self.__saldo -= monto
                print(f'El retiro de {monto} es Exitoso!')
                print(f'Saldo actual {self.__saldo}')
            else:
                print('No puedes retirar mas saldo de el que tiene')
        else:
            print('Debe ingresar un monto mayor que 0')


cliente1 = CuentaBancaria('Juan', 10000)

cliente1.consultarSaldo()

cliente1.depositar(20000)

cliente1.retirar(5000)