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