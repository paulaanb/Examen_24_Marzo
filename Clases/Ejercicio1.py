#Enunciado:Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.

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
        