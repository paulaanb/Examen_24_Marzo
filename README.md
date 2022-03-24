# Examen_24_Marzo
La direccion de este repositorio es [https://github.com/paulaanb/Examen_24_Marzo]

En el hemos intentado resolver lo que nos pedia el enunciado
 
 #Ejercicio 1:
 
 Enunciado:Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.
 
 
    class libro:
        def __init__ (nombre, autor, genero, añopublicacion, titulo, ISBN, edicion):
            self.nombre() = nombre libro
            self.autor() = autor
            self.genero() = genero
            self.añopublicacion() = año de publicacion
            self.titulo() = titulo
            self.ISBN() = ISBN
            self.edicion() = edicion
    
        #Definimos los metodos para acceder a la clase libro:
        def getnombre(self):
            return self.nombre
        def getautor(self):
            return self.autor
        def getgenero(self):
            return self.genero
        def getañodepublicacion(self):
            return self.añopublicacion
        def gettitulo(self):
            return self.titulo
        def getISBN(self):
            return self.ISBN
        def getedicion(self):
            return self.edicion

        def mostrarlibro(self):
            print("\nNombre: " + str(self.nombre()) + "\nAutor: " + self.autor() + "\nGenero: " + self.genero() + "\nAño de publicacion: " + str(self.añodepublicacion()) + "\nTitulo del libro: " + self.titulo() + "\nISBN: " + str(self.ISBN()) + "\nNumero de edicion: " + str(self.edicion()))

    #Definimos las variables:
    nombre= raw_input("Por favor, escriba el nombre del libro: ")
    autor = raw_input("Por favor, introduzca el nombre del autor del libro: ")
    genero = raw_input("Por favor, introduzca el genero al que pertenece el libro: ")
    añodepublicacion = input("Por favor, introduzca el año de publicacion del libro: ")
    titulo = raw_input("Por favor, introduca el titulo del libro: ")
    ISBN = input("Por favor, introduzca el ISBN del libro: ")
    edicion = input("Por favor, introduzca el numero de edicion del libro: ")

    paula = libro(nombre, autor, genero, añodepublicacion, titulo, ISBN, edicion)
    paula.mostrarlibro()


#Ejercicio 2:

Enunciado: Considere los objetos siguientes: Animal, Mamífero, Ovíparo, Pollo, Gato, Ornitorrinco
Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases.
Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX).
¿Es posible implementar estos objetos en Python?

    #Definimos la clase a utilizar
    class Animal:
        def __init__(self, nombre, especie):
            self.nombre = nombre
            self.especie = especie
    #Definimos los comandos necesarios
    def getnombre(self):
        return self.nombre
    def getespecie(self):
        return self.especie

    def mostrarAnimal(self):
        print("\nNombre: " + self.getnombre() + "\nEspecie: " + self.getespecie())

    #Establecemos las variables
    nombre = raw_input("Por favor, introduzca el tipo de animal: ")
    especie = raw_input("Por favor, introduzca la especie del animal: ")
    paula = Animal(nombre, especie)
    paula.mostrarAnimal()


#Ejercicio 3:

Enunciado:
Se pide crear una clase que refleje una cuenta bancaria. Esta clase va a tener cómo atributos el ID de la cuenta bancaria, el nombre de titular, una fecha de apertura, un número de cuenta y un saldo. Por favor, aplique el tipo que mejor corresponda a cada atributo. 
La cuenta bancaria deberá tener como mínimo un método para retirar dinero, otro para ingresar dinero y otro para transferir dinero de una cuenta bancaria a otra cuenta bancaria. De una cuenta bancaria no se podrá retirar nunca dinero (ni transferir) si la cantidad de dinero a retirar o transferir es mayor que el saldo.
Crea una cuenta bancaria a Plazo Fijo, en la cual cuando se retira dinero de algún modo antes de una Fecha de Vencimiento además del dinero a retirar se penaliza con un 5% adicional.
Crea además una cuenta Vip, que tendrá un atributo adicional que es el saldo negativo máximo que puede tener. En las cuentas Vip uno podrá tener saldo negativo siempre que no supere este valor.
A continuación, construye una aplicación que permita crear los tres tipos de cuentas. El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado, la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio de 12 dígitos. Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, transferir dinero de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €. 

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



