# Función para obtener las temperaturas diarias
def obtener_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingresa la temperatura del día {i + 1}: "))
                if temp < -100 or temp > 100:
                    print("Por favor, ingresa una temperatura mayor que -100ºC y menor que 100ºC.")
                else:
                    temperaturas.append(temp)
                    break
            except ValueError:
                print("Error: ingresa un número válido.")
    return temperaturas

# Función para calcular el promedio de la lista de temperaturas
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Función para obtener la temperatura máxima y mínima
def encontrar_max_min(lista):
    max_temp = max(lista)
    min_temp = min(lista)
    max_dia = lista.index(max_temp) + 1
    min_dia = lista.index(min_temp) + 1
    return max_temp, max_dia, min_temp, min_dia

# Mostrar alertas de temperaturas extremas
def mostrar_alertas(lista):
    for i, temp in enumerate(lista):
        if temp > 60:
            print(f"Alerta: el día {i + 1} superó los 60ºC con {temp}ºC.")
        elif temp < -40:
            print(f"Alerta: el día {i + 1} tuvo una temperatura bajo 0ºC con {temp}ºC.")

# Función principal
def main():
    print("Bienvenido al programa de temperaturas semanales.\n")

    # Paso 1: obtener la temperatura de los 7 días
    temperaturas = obtener_temperaturas()

    # Paso 2: calcular el promedio semanal
    promedio = calcular_promedio(temperaturas)

    # Paso 3: encontrar la temperatura máxima y mínima
    max_temp, max_dia, min_temp, min_dia = encontrar_max_min(temperaturas)

    # Paso 4: mostrar los resultados de manera amigable
    print("\nResultados del análisis de temperaturas:")
    print(f"La temperatura máxima fue {max_temp}ºC en el día {max_dia}.")
    print(f"La temperatura mínima fue {min_temp}ºC en el día {min_dia}.")
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}ºC.")

    # Paso 5: mostrar qué días estuvieron por encima del promedio
    print("\nDías con temperaturas por encima del promedio:")
    for i, temp in enumerate(temperaturas):
        if temp > promedio:
            print(f"Día {i + 1}: {temp}ºC.")

    # Mostrar alertas de temperaturas extremas
    mostrar_alertas(temperaturas)

if __name__ == "__main__":
    main()