#Enunciado:
#Considere los objetos siguientes: Animal, Mamífero, Ovíparo, Pollo, Gato, Ornitorrinco
#Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases.
#Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX).
#¿Es posible implementar estos objetos en Python?

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