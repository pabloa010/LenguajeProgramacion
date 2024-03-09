class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print (f'Se han depositado {cantidad} unidades.')
        else:
            print('La cantidad a depositar debe ser mayor que cero.')
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f'Se han retirado {cantidad} unidades.')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Su saldo actual es: {self.__saldo}')

mi_cuenta = CuentaBancaria(1000)

mi_cuenta.consultar_saldo()
mi_cuenta.depositar(-500)
mi_cuenta.depositar(200)
