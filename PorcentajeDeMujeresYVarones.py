# Solicitar al usuario la cantidad de mujeres y Varones
# Usamos la función input() para recibir datos del usuario y los convertimos a enteros con int()

cantidad_mujeres = int(input("Ingrese la cantidad de mujeres en el aula: "))
cantidad_varones = int(input("Ingrese la cantidad de varones en el aula: "))

# Calculamos el total de estudiantes
# La variable + (suma) se usa para sumar ambas cantidades
total_estudiantes = cantidad_mujeres + cantidad_varones

# Validamos que el total no sea cero para evitar errores de división entre cero
if total_estudiantes == 0:
    print("No hay estudiantes en el aula.")
else:
    # Paso 3: Calcular los porcentajes
    # Usamos la variable / para dividir y * para convertir el resultado a porcentaje (multiplicamos por 100)
    porcentaje_mujeres = (cantidad_mujeres / total_estudiantes) * 100
    porcentaje_varones = (cantidad_varones / total_estudiantes) * 100

    # Mostramos resultados
    # Usamos round() para redondear los resultados a 2 decimales
    print(f"Porcentaje de mujeres: {round(porcentaje_mujeres, 2)}%")
    print(f"Porcentaje de varones: {round(porcentaje_varones, 2)}%")
    # de vuelta usamos f antes de las comillas puesto a que debe de ser un f-string, que nos deja usar print y usar variables dentro de una string
    # el dos al final indica los dos decimales que operador round va a redondear a

    #input() → Permite ingresar datos desde el teclado.

# int() → Convierte una cadena (string) a número entero.
# + → Suma dos valores numéricos.
# / → Divide dos valores numéricos.
# * 100 → Convierte una fracción a porcentaje.
# round(variable, 2) → Redondea un número a dos cifras decimales.
# if → Estructura condicional para evitar errores si no hay estudiantes.