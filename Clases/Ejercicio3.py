#Enunciado:
#Se pide crear una clase que refleje una cuenta bancaria. Esta clase va a tener cómo atributos el ID de la cuenta bancaria, el nombre de titular, una fecha de apertura, un número de cuenta y un saldo. Por favor, aplique el tipo que mejor corresponda a cada atributo. 
#La cuenta bancaria deberá tener como mínimo un método para retirar dinero, otro para ingresar dinero y otro para transferir dinero de una cuenta bancaria a otra cuenta bancaria. De una cuenta bancaria no se podrá retirar nunca dinero (ni transferir) si la cantidad de dinero a retirar o transferir es mayor que el saldo.
#Crea una cuenta bancaria a Plazo Fijo, en la cual cuando se retira dinero de algún modo antes de una Fecha de Vencimiento además del dinero a retirar se penaliza con un 5% adicional.
#Crea además una cuenta Vip, que tendrá un atributo adicional que es el saldo negativo máximo que puede tener. En las cuentas Vip uno podrá tener saldo negativo siempre que no supere este valor.
#A continuación, construye una aplicación que permita crear los tres tipos de cuentas. El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado, la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio de 12 dígitos. Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €. 


#Definimos la clase a utilizar

class cuenta:
    def __init__(self, cuenta, propietario, estado, saldo, fechadeapertura):
        self.cuenta = cuenta
        self.propietario = propietario
        self.estado = estado
        self.saldo = saldo
        self.fechadeapertura = fecha de apertura

#Ahora empezamos a crear el metodo para retirar el dinero y para ingresarlo.
def setRetirar(self,s):
    if self.saldo - s > 0:
        self.saldo - s 
def setIngresara(self,s):
    self.saldo = self.saldo + s

#Creamos los metodos para accedor a la clase cuenta
def getcuenta(self):
    return self.cuenta
def getpropietario(self):
    return self.propietario
def getestado(self):
    return self.estado
def getsaldo(self):
    return self.saldo
def getfechadeapertura(self):
    return self.fechadeapertura

#Definimos mostrar cuenta
def mostrarcuenta(self):
    print("\nCuenta: " + self.getcuenta() + "\nPropietario: " + self.getpropietario() + "\nEstado: " + str(self.getestado()) + "\nSaldo: " + str(self.getsaldo()) + "\nFecha de apertura: " + str(self.getfechadeapertura()))

#Establecemos las variables:
cuenta = raw_input("Por favor, ingresa el numero de cuenta asociada: ")
propietario = raw_input("Por favor, ingresa el nombre del propetario: ")
saldo = raw_input("Por favor, ingresa el saldo inicial de la cuenta: ")
fechadeapertura =raw_input("Por favor, ingresa la fecha de apertura de la cuenta del banco: ")
paula = cuenta(cuenta, propetario, saldo, fechadeapertura)
paula.mostrarcuenta()



