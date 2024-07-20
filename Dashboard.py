import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script sea absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Defina la ruta base donde se encuentra este script
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'semana1/abstraccion.py',
        '2': 'semana1/encapsulacion.py',
        '3': 'semana1/herencia.py',
        '4': 'semana1/polimorfismo.py',
        '5': 'semana3/comparacion_POO.py',
        '6': 'semana3/comparacion_tradicional.py',
        '7': 'semana4/Ejemplos_del_Mundo_Real_y_Características_de_la_Programación_Orientada_a_Objetos.py',
        '8': 'semana5/Tipos_de_datos_Identificadores.py',
        '9': 'semana6/Clases_objetos_herencia_encapsulamiento_y_polimorfismo.py',
        '10': 'semana7/Implementación_de_Constructores_y_Destructores_en_Python.py'
    }

    while True:
        print("\nMenú Principal - Tablero de mandos")
        # Imprime las opciones del menú
        for clave in opciones:
            print(f"{clave} - {opciones[clave]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el camino sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el tablero
if __name__ == "__main__":
    mostrar_menu()
