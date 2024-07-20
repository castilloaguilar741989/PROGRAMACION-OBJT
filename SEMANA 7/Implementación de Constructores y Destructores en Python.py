class Persona:
    def __init__(self, nombre):
        """
        Constructor de la clase Persona.

        Args:
        nombre (str): Nombre de la persona.
        """
        self.nombre = nombre
        print(f'Se ha creado una nueva persona llamada {self.nombre}.')

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se activa cuando el objeto persona es eliminado de la memoria.
        """
        print(f'La persona {self.nombre} ha sido eliminada.')

# Ejemplo de uso de la clase Persona
persona1 = Persona('Juan')
persona2 = Persona('María')

# Eliminamos el objeto persona1 antes de finalizar el programa
del persona1

# Al finalizar el programa, se eliminan automáticamente los objetos restantes
