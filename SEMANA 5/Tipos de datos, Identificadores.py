# Programa para gestionar información básica de un registro de empleados

# Definir una clase para representar un empleado
class Empleado:
    def __init__(self, nombre, edad, salario):
        """
        Inicializa un objeto Empleado con nombre, edad y salario.

        :param nombre: Nombre del empleado.
        :param edad: Edad del empleado.
        :param salario: Salario del empleado.
        """
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def mostrar_informacion(self):
        """
        Muestra la información del empleado.

        :return: Una cadena con la información del empleado.
        """
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: ${self.salario}"

# Crear un empleado utilizando la clase Empleado
empleado1 = Empleado("Juan Perez", 30, 2500.0)

# Mostrar la información del empleado creado
print("Información del Empleado:")
print(empleado1.mostrar_informacion())
