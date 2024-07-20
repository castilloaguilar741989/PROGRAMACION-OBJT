def ingresar_temperaturas_diarias():
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

def main():
    temperaturas_diarias = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
    print(f"El promedio de temperaturas de la semana es: {promedio_semanal}")

if __name__ == "__main__":
    main()

