class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Este método será implementado de manera específica en las subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu muu"

# Función para hacer sonidos de varios animales
def hacer_sonidos(animales):
    for animal in animales:
        print(f"{animal.nombre}: {animal.hacer_sonido()}")

# Crear instancias de diferentes animales
mi_perro = Perro("Buddy")
mi_gato = Gato("Milo")
mi_vaca = Vaca("Daisy")

# Llamar a la función de hacer sonidos con diferentes animales
hacer_sonidos([mi_perro, mi_gato, mi_vaca])
