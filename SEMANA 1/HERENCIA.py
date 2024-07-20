class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} está maullando.")

# Crear instancias de Perro y Gato
mi_perro = Perro("Buddy", "Labrador")
mi_gato = Gato("Milo", "Negro")

# Acceder a los métodos de las clases base y subclases
mi_perro.comer()   # Salida: Buddy está comiendo.
mi_perro.ladrar()  # Salida: Buddy está ladrando.

mi_gato.comer()    # Salida: Milo está comiendo.
mi_gato.maullar()  # Salida: Milo está maull