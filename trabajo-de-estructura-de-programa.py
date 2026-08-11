def programa_osciloscopio():
	# Inicialización de variables requeridas
	umbral_pico = 5.0
	pico_maximo = 0.0
	contador_peligrosos = 0
	suma_amplitud = 0.0
	contador_amplitud = 0

	while True:
		print("\n--- MENÚ DEL PROGRAMA ---")
		print("1. Registrar amplitudes de señal")
		print("2. Detectar picos peligrosos")
		print("3. Calcular promedio de amplitud")
		print("4. Salir")

		opcion = input("Seleccione una opción (1-4): ").strip()

		if opcion == "1":
			try:
				amplitud = float(input("Ingrese el valor de amplitud (0 - 20): "))

				# Validación del rango permitido
				if 0 <= amplitud <= 20:
					contador_amplitud += 1
					suma_amplitud += amplitud

					# Actualización de pico máximo
					if contador_amplitud == 1 or amplitud > pico_maximo:
						pico_maximo = amplitud

					# Evaluación de umbral de riesgo
					if amplitud > umbral_pico:
						contador_peligrosos += 1

					print(f"Amplitud {amplitud} registrada correctamente.")
				else:
					print("Error: La amplitud debe estar dentro del rango 0 <= amplitud <= 20.")
			except ValueError:
				print("Error: Debe ingresar un valor numérico válido.")

		elif opcion == "2":
			if contador_amplitud == 0:
				print("No hay mediciones registradas.")
			else:
				print(f"\n--- DETECCIÓN DE PICOS PELIGROSOS ---")
				print(f"Pico máximo registrado: {pico_maximo}")
				print(f"Contador de picos peligrosos (> {umbral_pico}): {contador_peligrosos}")

				if contador_peligrosos > 0:
					print("Mensaje: La señal presenta picos que pueden dañar el circuito.")
				else:
					print("Mensaje: La señal se mantiene dentro de rangos seguros.")

		elif opcion == "3":
			if contador_amplitud == 0:
				print("No hay mediciones registradas.")
			else:
				promedio = suma_amplitud / contador_amplitud
				print(f"\n--- INFORME DE PROMEDIO Y ESTADO ---")
				print(f"Pico máximo registrado: {pico_maximo}")
				print(f"Picos peligrosos detectados: {contador_peligrosos}")
				print(f"Promedio de amplitud: {promedio:.2f}")

				if contador_peligrosos > 0:
					print("Mensaje: La señal presenta picos que pueden dañar el circuito.")
				else:
					print("Mensaje: La señal se mantiene dentro de rangos seguros.")

		elif opcion == "4":
			print("Saliendo del programa...")
			break
		else:
			print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
	programa_osciloscopio()

