def sistema_iluminacion():
    # Variables iniciales según el caso
    umbral_luz = 50
    contador_activaciones = 0
    contador_mediciones = 0
    suma_luz = 0.0
    nivel_luz = None

    # Variable de control extra para no contar la misma medición dos veces
    medicion_evaluada = True

    while True:
        print("\n" + "="*35)
        print(" Caso 9. Iluminación Inteligente")
        print("="*35)
        print("1. Registrar niveles de luz.")
        print("2. Activar lámpara según umbral.")
        print("3. Mostrar estadísticas de iluminación.")
        print("4. Salir del programa.")
        print("="*35)

        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            # Validación: nivel_luz numérico y 0 <= nivel_luz <= 1000
            while True:
                entrada = input("Ingresa el nivel de luz detectado (0 - 1000): ")
                try:
                    valor = float(entrada)
                    if 0 <= valor <= 1000:
                        nivel_luz = valor
                        suma_luz += nivel_luz
                        contador_mediciones += 1
                        medicion_evaluada = False  # Hay una nueva medición sin evaluar
                        print(f"Nivel de luz ({nivel_luz}) registrado exitosamente.")
                        break
                    else:
                        print("Error: El valor debe estar en el rango de 0 a 1000.")
                except ValueError:
                    print("Error: Debes ingresar un valor numérico válido.")

        elif opcion == '2':
            if nivel_luz is None:
                print("Error: Aún no has registrado ningún nivel de luz (Ve a la Opción 1).")
            else:
                if not medicion_evaluada:
                    if nivel_luz < umbral_luz:
                        print("Lámpara activada")
                        contador_activaciones += 1
                    else:
                        print("Lámpara apagada")
                    medicion_evaluada = True
                else:
                    if nivel_luz < umbral_luz:
                        print("La lámpara ya se encontraba activada con el último registro.")
                    else:
                        print("La lámpara ya se encontraba apagada con el último registro.")

        elif opcion == '3':
            print("\n--- Estadísticas de Iluminación ---")
            print(f"Activaciones de la lámpara: {contador_activaciones}")

            if contador_mediciones > 0:
                promedio = suma_luz / contador_mediciones
                print(f"Promedio de iluminación: {promedio:.2f}")

                if promedio >= umbral_luz:
                    print("Estado: Ambiente correctamente iluminado")
                else:
                    print("Estado: Iluminación insuficiente")
            else:
                print("No se puede calcular el promedio (0 mediciones).")

        elif opcion == '4':
            print("Saliendo del sistema de iluminación inteligente... ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 4.")


if __name__ == "__main__":
    sistema_iluminacion()
