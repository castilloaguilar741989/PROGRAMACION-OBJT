class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida. Debe ser un número positivo.")

# Crear una instancia de Persona
persona = Persona("Juan", 30)

# Acceder a los atributos de manera controlada mediante getters y setters
print(persona.get_nombre())  # Salida: Juan
print(persona.get_edad())    # Salida: 30

persona.set_nombre("Pedro")
persona.set_edad(25)

print(persona.get_nombre())  # Salida: Pedro
print(persona.get_edad())    # Salida: 25

# Intentar acceder directamente a los atribut