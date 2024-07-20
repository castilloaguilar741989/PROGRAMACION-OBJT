class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) != 7:
            raise ValueError("Debe ingresar temperaturas diarias para cada día de la semana.")
        return sum(self.temperaturas) / len(self.temperaturas)

class ClimaSemanal(ClimaDiario):
    def __init__(self):
        super().__init__()

    def ingresar_temperaturas_semanales(self, temperaturas_semanales):
        if len(temperaturas_semanales) != 7:
            raise ValueError("Debe ingresar temperaturas diarias para cada día de la semana.")
        self.temperaturas = temperaturas_semanales

def main():
    # Ejemplo de uso de la clase ClimaDiario
    clima_diario = ClimaDiario()
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        clima_diario.ingresar_temperatura_diaria(temperatura)
    promedio_semanal_diario = clima_diario.calcular_promedio_semanal()
    print(f"El promedio de temperaturas de la semana (ClimaDiario) es: {promedio_semanal_diario}")

    # Ejemplo de uso de la clase ClimaSemanal
    temperaturas_semanales = []
    for dia in range(1, 8):