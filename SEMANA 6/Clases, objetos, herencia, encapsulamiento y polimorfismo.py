# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido (Encapsulación)
        self._edad = edad  # Atributo protegido (Encapsulación)

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

    def __str__(self):
        return f"{self._nombre} tiene {self._edad} años"


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza  # Atributo protegido (Encapsulación)

    def hacer_sonido(self):
        return "Guau"

    def __str__(self):
        return f"{self._nombre} es un {self._raza} y tiene {self._edad} años"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color  # Atributo protegido (Encapsulación)

    def hacer_sonido(self):
        return "Miau"

    def __str__(self):
        return f"{self._nombre} es un gato de color {self._color} y tiene {self._edad} años"


# Polimorfismo a través de métodos sobrescritos
def imprimir_sonido(animal):
    print(f"{animal._nombre} hace el sonido: {animal.hacer_sonido()}")


# Crear instancias y utilizar métodos
if __name__ == "__main__":
    # Crear instancias de Perro y Gato
    perro = Perro("Rex", 5, "Labrador")
    gato = Gato("Mimi", 3, "Blanco")

    # Imprimir detalles y sonidos
    print(perro)  # Rex es un Labrador y tiene 5 años
    imprimir_sonido(perro)  # Rex hace el sonido: Guau

    print(gato)  # Mimi es un gato de color Blanco y tiene 3 años
    imprimir_sonido(gato)  # Mimi hace el sonido: Miau
